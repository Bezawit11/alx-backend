#!/usr/bin/python3
"""3-lru_cache.py"""


BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system
    """
    cache = {}

    def __init__(self):
        """Initializes"""
        super().__init__()

    def put(self, key, item):
        """assign to the dict cache_data the item value for the key"""
        if key is None or item is None:
            return
        if key in self.cache:
            self.cache[key] = item
            self.cache_data = self.cache
            return
        if len(self.cache) == BaseCaching.MAX_ITEMS:
            a = list(self.cache.keys())[-1]
            print(f"DISCARD: {a}")
            self.cache.pop(a)
            self.cache_data = self.cache
        self.cache[key] = item
        self.cache_data = self.cache

    def get(self, key):
        """gets values from dictionary by referencing a key
        """
        if key is None or key not in self.cache:
            return None
        v = self.cache[key]
        self.cache.pop(key)
        self.cache[key] = v
        return self.cache[key]
  
