#!/usr/bin/python3
"""
	0-basic_async_syntax
"""
import asyncio
import random

async def wait_random(max_delay=10):
	"""
		waits for a random delay between 0 abnd max_delay
	"""
	delay = random.uniform(0, max_delay)
	await asyncio.sleep(delay)
	return delay
