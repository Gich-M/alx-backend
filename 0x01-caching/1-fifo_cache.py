#!/usr/bin/env python3
"""FIFO caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """A FIFO (First In First Out) cache implementation.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache.

        If cache is full, removes the first item added (FIFO).

        Args:
            key: The key to identify the item
            item: The value to store

        Returns:
            None
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {first_key}")

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
