#!/usr/bin/python3
"""3-lru_cache.py"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system
    """
    cache = OrderedDict()

    def __init__(self):
        """Initializes"""
        super().__init__()

    def put(self, key, item):
        """assign to the dict cache_data the item value for the key"""
        if key is None or item is None:
            return
        self.cache[key] = item
        self.cache.move_to_end(key)
        if len(self.cache) > BaseCaching.MAX_ITEMS:
            a = list(self.cache.keys())[0]
            print(f"DISCARD: {a}")
            self.cache.popitem(last = False)
        self.cache_data=self.cache.copy()

    def get(self, key):
        """gets values from dictionary by referencing a key
        """
        if key is None:
            return None
        if key not in self.cache:
            return
        self.cache.move_to_end(key)
        return self.cache[key]
