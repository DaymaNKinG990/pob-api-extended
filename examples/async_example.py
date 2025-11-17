"""Example of using async functionality in pobapi."""

import asyncio

# Note: This requires aiohttp to be installed
# pip install aiohttp

try:
    import aiohttp
except ImportError:
    print("aiohttp is required for async examples. Install with: pip install aiohttp")
    exit(1)

from pobapi.factory import BuildFactory
from pobapi.interfaces import AsyncHTTPClient


class AioHTTPClient(AsyncHTTPClient):
    """aiohttp implementation of AsyncHTTPClient."""

    async def get(self, url: str, timeout: float = 6.0) -> str:
        """
        Fetch the text content at the given URL, normalizing Pastebin
        paste links to their raw form.

        If the URL is a Pastebin paste (https://pastebin.com/<id>), it
        will be converted to the raw paste URL before fetching. Performs
        an HTTP GET and returns the response body as text; HTTP error
        responses raise an exception.

        Parameters:
            url (str): The resource URL to fetch. Pastebin paste URLs are
                converted to their raw endpoint.
            timeout (float): Total request timeout in seconds (default 6.0).

        Returns:
            str: The response body as text.

        Raises:
            aiohttp.ClientResponseError: If the response has an HTTP error status.
            aiohttp.ClientError: For other client/network related errors.
        """
        raw = url.replace("https://pastebin.com/", "https://pastebin.com/raw/")
        async with aiohttp.ClientSession() as session:
            async with session.get(
                raw, timeout=aiohttp.ClientTimeout(total=timeout)
            ) as response:
                response.raise_for_status()
                return await response.text()


async def main():
    """
    Demonstrates fetching builds asynchronously using AioHTTPClient and
    BuildFactory.

    Creates an AioHTTPClient and a BuildFactory, then fetches a build
    from a paste URL and from an import code, printing selected build
    attributes and printing errors if operations fail.
    """
    # Create factory with async HTTP client
    http_client = AioHTTPClient()
    factory = BuildFactory(async_http_client=http_client)

    # Fetch build from URL asynchronously
    url = "https://pastebin.com/your-pastebin-id"
    try:
        build = await factory.async_from_url(url)
        print(f"Build class: {build.class_name}")
        print(f"Level: {build.level}")
        print(f"Life: {build.stats.life}")
    except Exception as e:
        print(f"Error: {e}")

    # Or from import code
    import_code = "your-import-code-here"
    try:
        build = await factory.async_from_import_code(import_code)
        print(f"Build class: {build.class_name}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
