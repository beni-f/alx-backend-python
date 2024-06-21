#!/usr/bin/env python3
"""
    Let's duck type an iterable object
"""
from typing import Sequence, List, Tuple


def element_length(lst: Sequence) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
