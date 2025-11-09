#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset
    
    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset
    
    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert type(index) is int
        assert type(page_size) is int
        assert index > 0
        assert page_size > 0
        assert index < len(self.dataset())

        content = [self.indexed_dataset().get(i) for i in range(index, index + page_size)]
        a = 1
        null_value = content.count(None)

        for a in range(null_value):
            content.remove(None)
            content.append(self.indexed_dataset().get(index + page_size + a))
            a += 1

        return {
            "index": index,
            "next_index": index + page_size if self.indexed_dataset().get(index + page_size) else None,
            "page_size": len(content),
            "data": content
        }