#!/usr/bin/env python3
"""
0-basic_async_syntax
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
        waits for a random delay between 0 abnd max_delay
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
