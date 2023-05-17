#!/usr/bin/python3
"""1-fifo_cache.py"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """inherits from BaseCaching and is a caching system
    """
    m = []
    def __init__(self):
        """Initializes"""
        super().__init__()

    def put(self, key, item):
        """ assign to the dict cache_data the item value for the key"""
        if key is None or item is None:
            return
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.m.append(key)
            return
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            a = self.m[-1]
            self.cache_data.pop(a)
            print(f"DISCARD: {a}")
        self.cache_data[key] = item
        self.m.append(key)

    def get(self, key):
        """gets values from dictionary by referencing a key
        """
        if key is None:
            return None
        if key in self.cache_data.keys():
            v = self.cache_data[key]
            return v
