#!/usr/bin/python3
"""3-lru_cache.py"""


from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system
    """
    cache = OrderedDict()

    def __init__(self):
        """Initializes"""
        super().__init__()

    def put(self, key, item):
        """assign to the dict cache_data the item value for the key"""
        k = []
        if key is None or item is None:
            return
        if key not in self.m.keys():
            self.m[key] = 0
        if key in self.m.keys():
            self.m[key] += 1
        print(self.m)
        a = 0
        h = []
        s_ = sorted(self.m.items(), key=lambda x:x[1])
        b = 0
        j = 0
        if len(self.cache) == BaseCaching.MAX_ITEMS:
            a = s_[0][0]
            print(f"DISCARD: {a}")
            self.cache.pop(a)
            self.m.pop(a)
        self.cache[key] = item
        self.cache_data = self.cache.copy()

    def get(self, key):
        """gets values from dictionary by referencing a key
        """
        d = {}
        if key is None:
            return None
        if key in self.cache_data.keys():
            v = self.cache_data[key]
            self.m[key] += 1
            return v
