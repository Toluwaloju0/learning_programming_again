#!/usr/bin/env python3
""" a function to get the objects to be used when quering a list item"""

def index_range(page, page_size):
    """ a function to get the index of items to be accessed from a page
    Args:
        page: a number to to get tthe start page
        page_size: a number to show how many items should be in a page
    return a tuple containing the start and end items of a page
    """

    return (((page - 1) * page_size), (page * page_size))


import csv
import math
from typing import List
class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"
    def __init__(self):
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
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0

        page_range: tuple = index_range(page, page_size)

        if len(self.dataset()) < page_range[0]:
            return []
        return self.dataset()[page_range[0]: page_range[1]]