#!/usr/bin/env python3
"""Measures the total execution time for wait_n(n, max_delay)"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay), and
    Returns total_time (total execution time) / n
    """
    begin_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return (end_time - begin_time) / n
