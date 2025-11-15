"""Caching module for pobapi."""

import hashlib
import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar

__all__ = ["Cache", "cached", "clear_cache"]

T = TypeVar("T")


class Cache:
    """Simple in-memory cache with TTL support."""

    def __init__(self, default_ttl: int = 3600, max_size: int = 1000):
        """Initialize cache.

        :param default_ttl: Default time-to-live in seconds (default: 1 hour).
        :param max_size: Maximum number of cached items (default: 1000).
        """
        self._cache: dict[str, tuple[Any, float]] = {}
        self._default_ttl = default_ttl
        self._max_size = max_size

    def get(self, key: str) -> Any | None:
        """Get value from cache.

        :param key: Cache key.
        :return: Cached value or None if not found or expired.
        """
        if key not in self._cache:
            return None

        value, expiry_time = self._cache[key]
        if time.time() > expiry_time:
            # Expired, remove from cache
            del self._cache[key]
            return None

        return value

    def set(self, key: str, value: Any, ttl: int | None = None) -> None:
        """Set value in cache.

        :param key: Cache key.
        :param value: Value to cache.
        :param ttl: Time-to-live in seconds. Uses default if None.
        """
        # Evict oldest entries if cache is full
        if len(self._cache) >= self._max_size and key not in self._cache:
            self._evict_oldest()

        ttl = ttl or self._default_ttl
        expiry_time = time.time() + ttl
        self._cache[key] = (value, expiry_time)

    def clear(self) -> None:
        """Clear all cached values."""
        self._cache.clear()

    def delete(self, key: str) -> None:
        """Delete specific key from cache.

        :param key: Cache key to delete.
        """
        self._cache.pop(key, None)

    def _evict_oldest(self) -> None:
        """Evict oldest entry from cache."""
        if not self._cache:
            return

        # Find oldest entry (lowest expiry time)
        oldest_key = min(self._cache.keys(), key=lambda k: self._cache[k][1])
        del self._cache[oldest_key]

    def size(self) -> int:
        """Get current cache size.

        :return: Number of cached items.
        """
        return len(self._cache)

    def stats(self) -> dict[str, Any]:
        """Get cache statistics.

        :return: Dictionary with cache statistics.
        """
        return {
            "size": len(self._cache),
            "max_size": self._max_size,
            "default_ttl": self._default_ttl,
        }


# Global cache instance
_default_cache = Cache(default_ttl=3600, max_size=1000)


def _make_key(*args, **kwargs) -> str:
    """Create cache key from function arguments.

    :param args: Positional arguments.
    :param kwargs: Keyword arguments.
    :return: Cache key as string.
    """
    # Create a hash of the arguments
    key_data = str(args) + str(sorted(kwargs.items()))
    return hashlib.md5(key_data.encode()).hexdigest()


def cached(ttl: int | None = None, cache_instance: Cache | None = None):
    """Decorator for caching function results.

    :param ttl: Time-to-live in seconds. Uses cache default if None.
    :param cache_instance: Cache instance to use. Uses default if None.
    :return: Decorated function.
    """
    cache = cache_instance or _default_cache

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @wraps(func)
        def wrapper(*args, **kwargs) -> T:
            key = f"{func.__module__}.{func.__name__}:{_make_key(*args, **kwargs)}"
            cached_value = cache.get(key)
            if cached_value is not None:
                return cached_value  # type: ignore[no-any-return]

            result = func(*args, **kwargs)
            cache.set(key, result, ttl=ttl)
            return result

        return wrapper

    return decorator


def clear_cache() -> None:
    """Clear the default cache."""
    _default_cache.clear()


def get_cache() -> Cache:
    """Get the default cache instance.

    :return: Default cache instance.
    """
    return _default_cache
