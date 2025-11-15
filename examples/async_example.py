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
        """Fetch content from URL asynchronously."""
        raw = url.replace("https://pastebin.com/", "https://pastebin.com/raw/")
        async with aiohttp.ClientSession() as session:
            async with session.get(
                raw, timeout=aiohttp.ClientTimeout(total=timeout)
            ) as response:
                response.raise_for_status()
                return await response.text()


async def main():
    """Example async usage."""
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
