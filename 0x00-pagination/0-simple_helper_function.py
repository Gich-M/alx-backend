#!/usr/bin/env python3
"""Module simple helper function."""


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
