#!/usr/bin/env python3
"""
    4-tasks
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Spawn task_wait_random n times with the specified max_delay
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    sorted_results = []
    while results:
        min_result = min(results)
        sorted_results.append(min_result)
        results.remove(min_result)

    return sorted_results