#!/usr/bin/env python3
"""
This module defines a type-annotated function `zoom_array` that takes a tupl
and returns a list.
"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Return a list of tuples zoomed in `factor` times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
