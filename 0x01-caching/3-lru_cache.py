#!/usr/bin/env python3
"""LRU caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """An LRU (Least Recently Used) cache implementation.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        If cache is full, removes the least recently used item (LRU).
        Updates item's position if key exists.

        Args:
            key: The key to identify the item
            item: The value to store

        Returns:
            None
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {lru_key}")

            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by key.

        Updates access order of the accessed item.

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if not found
        """
        if key is not None and key in self.cache_data:
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None
