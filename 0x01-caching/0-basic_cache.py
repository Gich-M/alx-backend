#!/usr/bin/env python3

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and
        is a caching system without a limit.
    """

    def put(self, key, item):
        """"
        Adds an item to the cache.

        Args:
            key: Key for the item
            item: Item to be stored

        Return:
            None
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieves an item from the cache using its key.

        Args:
            key: Key for the item

        Return:
            Item from the cache or None if not found
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
