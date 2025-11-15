"""Async utilities for pobapi."""

import base64
import logging
import zlib

from pobapi.exceptions import (
    InvalidImportCodeError,
    InvalidURLError,
    NetworkError,
)
from pobapi.interfaces import AsyncHTTPClient

logger = logging.getLogger(__name__)


async def _fetch_xml_from_url_async(
    url: str, http_client: AsyncHTTPClient | None = None, timeout: float = 6.0
) -> bytes:
    """Get a Path Of Building import code from URL asynchronously.

    :param url: pastebin.com URL.
    :param http_client: Optional async HTTP client. If None, raises error.
    :param timeout: Request timeout.
    :return: Decompressed XML build document.
    :raises: InvalidURLError, NetworkError
    """
    if not url.startswith("https://pastebin.com/"):
        raise InvalidURLError(f"{url} is not a valid pastebin.com URL.")

    if http_client is None:
        raise ValueError("Async HTTP client is required for async operations")

    try:
        response_text = await http_client.get(url, timeout=timeout)
        return await _fetch_xml_from_import_code_async(response_text)
    except Exception as e:
        if isinstance(e, InvalidURLError | InvalidImportCodeError):
            raise
        logger.exception("Network error in async request")
        raise NetworkError(f"Async request failed: {str(e)}") from e


async def _fetch_xml_from_import_code_async(import_code: str) -> bytes:
    """Decodes and unzips a Path Of Building import code asynchronously.

    :param import_code: Import code string.
    :return: Decompressed XML build document.
    :raises: InvalidImportCodeError
    """
    if not import_code or not isinstance(import_code, str):
        raise InvalidImportCodeError("Import code must be a non-empty string")

    try:
        # These operations are CPU-bound but fast, so we can run them
        # in the event loop without blocking significantly
        base64_decode = base64.urlsafe_b64decode(import_code)
        decompressed_xml = zlib.decompress(base64_decode)
    except (TypeError, ValueError) as e:
        logger.exception("Error while decoding.")
        raise InvalidImportCodeError("Failed to decode import code") from e
    except zlib.error as e:
        logger.exception("Error while decompressing.")
        raise InvalidImportCodeError("Failed to decompress import code") from e

    return decompressed_xml
