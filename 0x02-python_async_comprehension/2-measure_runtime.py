#!/usr/bin/env python3
"""
    Run time for four parallel comprehensions
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
        Measure time
    """
    start_time = time.perf_counter()
    asyncComprehension = [async_comprehension() for i in range(4)]
    await asyncio.gather(*asyncComprehension)
    end_time = time.perf_counter()
    return end_time - start_time
