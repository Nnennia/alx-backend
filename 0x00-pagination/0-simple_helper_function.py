#!/usr/bin/env python3
"""Function that returns a tuple of size two
containing a start index and an end index"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple of size two containing a start index and an end index"""
    end = int(page * page_size)
    start = int(end - page_size)
    return start, end
