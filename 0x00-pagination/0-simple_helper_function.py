#!/usr/bin/env python3
"""pagination"""


def index_range(page, page_size):
    """ppagination"""
    a = page_size * page
    b = a - page_size
    return (b, a)
