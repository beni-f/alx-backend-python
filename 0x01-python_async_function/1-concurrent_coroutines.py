#!/usr/bin/env python3
"""
1-concurrent_coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Spawn wait_random n times with the specified max_delay
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    sorted_results = []
    while results:
        min_result = min(results)
        sorted_results.append(min_result)
        results.remove(min_result)

    return sorted_results
