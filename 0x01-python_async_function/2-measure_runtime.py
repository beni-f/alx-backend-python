#!/usr/bin/env python3
"""
    2-measure_runtime
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
        Measures the total execution time for the wait_n function on average
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()

    total_time = time.perf_counter()
    return total_time / n
