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
        """
        Return a page of data that is resilient to deletions.

        Args:
            index: Starting index of the current page
            page_size: Size of the page

        Return:
            Dict: Dictionary containing the page data and pagination metadata
        """
        data = self.indexed_dataset()

        assert isinstance(index, int) and 0 <= index < len(self.dataset())
        current_page_data = []
        next_index = index
        items_collected = 0

        while items_collected < page_size and next_index < len(self.dataset()):
            if next_index in data:
                current_page_data.append(data[next_index])
                items_collected += 1
            next_index += 1

        return {
            'index': index,
            'data': current_page_data,
            'page_size': page_size,
            'next_index': next_index
        }
