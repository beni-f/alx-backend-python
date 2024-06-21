#!/usr/bin/env python3
"""
    Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        Takes a float multiplier as argument\
        and returns a function that multiplies a float by multiplier.
    """
    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
