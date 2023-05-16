#!/usr/bin/env python3
"""pagination"""

import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """pagination"""
    a = page_size * page
    b = a - page_size
    return (b, a)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """initialization"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        file = open(self.DATA_FILE, "r")
        data = list(csv.reader(file, delimiter=","))
        file.close()
        r = index_range(page, page_size)
        a = r[0] + 1
        b = r[1] + 1
        return data[a:b]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary"""
        file = open(self.DATA_FILE, "r")
        data = list(csv.reader(file, delimiter=","))
        file.close()
        s = len(data) - 1
        total_pages = math.ceil(s / page_size)
        if page + 1 > total_pages:
            n = None
        else:
            n = page + 1
        if page - 1 == 0:
            p = None
        else:
            p = page - 1
        d = {"page_size": page_size,
             "page": page,
             "data": self.get_page(page, page_size),
             "next_page": n,
             "prev_page": p,
             "total_pages": total_pages
             }
        return d
