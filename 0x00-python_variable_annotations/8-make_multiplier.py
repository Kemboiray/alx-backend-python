#!/usr/bin/env python3
"""
This module defines a type-annotated function `make_multiplier` that takes
a float `multiplier` as argument and returns a function that multiplies a
float by `multiplier`.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by `multiplier`.
    """
    def multiply_by_multiplier(number: float) -> float:
        """
        Returns the product of `number` and `multiplier`.
        """
        return number * multiplier
    return multiply_by_multiplier
