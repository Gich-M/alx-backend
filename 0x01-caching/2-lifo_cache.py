#!/usr/bin/env python3
"""LIFO caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """A LIFO (Last In First Out) cache implementation.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        If cache is full, removes the last item added (LIFO).

        Args:
            key: The key to identify the item
            item: The value to store

        Returns:
            None
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem()
                print(f"DISCARD: {last_key}")

            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key.

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if not found
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
