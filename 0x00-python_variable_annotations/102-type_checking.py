#!/usr/bin/env python3
"""
    Type Checking
"""
from typing import Tuple, List, Optional


def zoom_array(lst: Tuple, factor: int = 2) -> List[int]:
    """
        Zoom Array
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
