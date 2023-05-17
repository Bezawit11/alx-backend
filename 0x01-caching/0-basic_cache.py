#!/usr/bin/python3
"""0-basic_cache.py"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """appends a key and value pair to dictionary
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        
    def get(self, key):
        """gets values from dictionary by referencing a key
        """
        if key is None:
            return None
        if key in self.cache_data.keys():
            v = self.cache_data[key]
            return v

