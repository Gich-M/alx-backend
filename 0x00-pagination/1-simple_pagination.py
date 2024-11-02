#!/usr/bin/env python3
"""Module simple helper function."""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> int:
    """
    Return a tuple of size two containing a start index
        and an end index corresponding to the range of
        indexes to return in a list for those
        particular pagination parameters.
    Args:
        page: The page
        page_size: The number of items per page
    Return:
        A tuple containing start and end indices
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """
        Retrieve a specific page of data from the dataset.

        Args:
            page (int): Page number (1-indexed)
            page_size (int): Number of items per page

        Returns:
            List[List]: List of rows for the requested page
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        data = self.dataset()

        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []
