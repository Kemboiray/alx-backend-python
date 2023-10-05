#!/usr/bin/env python3
"""
This module defines a type-annotated function `sum_mixed_list` which takes a
mixed list of integers and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Return the sum of a mixed list of integers and floats as a float.
    """
    return sum(mxd_lst)
