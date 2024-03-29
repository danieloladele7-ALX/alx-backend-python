#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Take the code from wait_n (task 1) and alter it into a new
    function task_wait_n. The code is nearly identical to wait_n
    except task_wait_random is being called.
    Returns the list of all the delays (float values).
    """
    futures = [task_wait_random(max_delay) for _ in range(n)]
    futures = asyncio.as_completed(futures)
    delays = [await future for future in futures]
    return delays
