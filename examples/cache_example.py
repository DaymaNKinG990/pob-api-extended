"""Example of using caching functionality in pobapi."""

from pobapi import clear_cache, get_cache
from pobapi.api import from_import_code

# Caching is automatically enabled for:
# - Import code decoding (1 hour TTL)
# - Skill tree parsing (24 hours TTL)

# Example: Multiple requests with same import code
import_code = "your-import-code-here"

# First call - will decode and cache
build1 = from_import_code(import_code)
print(f"First call - Build class: {build1.class_name}")

# Second call - will use cache (much faster)
build2 = from_import_code(import_code)
print(f"Second call - Build class: {build2.class_name}")

# Check cache statistics
cache = get_cache()
stats = cache.stats()
print(f"Cache size: {stats['size']}")
print(f"Max size: {stats['max_size']}")
print(f"Default TTL: {stats['default_ttl']} seconds")

# Clear cache if needed
clear_cache()
print("Cache cleared")
