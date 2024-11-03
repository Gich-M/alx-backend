#!/usr/bin/env python3
"""LFU caching module.
"""
from base_caching import BaseCaching
from collections import OrderedDict, defaultdict


class LFUCache(BaseCaching):
    """An LFU (Least Frequently Used) cache implementation with LRU tiebreaker.
    Inherits from BaseCaching.
    """

    def __init__(self):
        """Initialize the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequencies = defaultdict(int)
        self.frequency_lists = defaultdict(OrderedDict)
        self.min_frequency = 0

    def update_frequency(self, key):
        """Update frequency count and position for accessed key.

        Args:
            key: The key being accessed
        """
        freq = self.frequencies[key]
        self.frequencies[key] += 1

        del self.frequency_lists[freq][key]

        if not self.frequency_lists[freq] and freq == self.min_frequency:
            self.min_frequency += 1

        self.frequency_lists[freq + 1][key] = None

    def put(self, key, item):
        """Add an item to the cache.

        If cache is full, removes the least frequently used item.
        If there's a tie, removes the least recently used item.

        Args:
            key: The key to identify the item
            item: The value to store

        Returns:
            None
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.update_frequency(key)
                return

            if len(self.cache_data) >= self.MAX_ITEMS:
                lfu_key, _ = self.frequency_lists[self.min_frequency].popitem(
                    last=False)
                del self.cache_data[lfu_key]
                del self.frequencies[lfu_key]
                print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.frequencies[key] = 0
            self.min_frequency = 0
            self.frequency_lists[0][key] = None

    def get(self, key):
        """Retrieve an item from the cache by key.

        Updates item frequency and access order.

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or None if not found
        """
        if key is not None and key in self.cache_data:
            self.update_frequency(key)
            return self.cache_data[key]
        return None
