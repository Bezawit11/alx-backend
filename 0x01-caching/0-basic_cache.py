#!/usr/bin/python3
"""0-basic_cache.py"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")

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

