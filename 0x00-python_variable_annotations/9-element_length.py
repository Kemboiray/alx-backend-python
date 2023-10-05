#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
This module defines a function `element_length` that takes as argument an
iterable containing sized items as elements and returns a list of tuples
consisting of the elements and their lengths.
"""

from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples consisting of the elements and their lengths.

    Parameters
    ----------
    lst : Iterable[Sequence]
        An iterable containing iterables as elements.

    Returns
    -------
    List[Tuple[Sequence, int]]
        A list of tuples consisting of the elements and their lengths.

    Examples
    --------
    >>> element_length([[1, 2, 3], [4, 5]])
    [([1, 2, 3], 3), ([4, 5], 2)]
    """
    return [(i, len(i)) for i in lst]
