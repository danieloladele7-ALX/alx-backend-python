#!/usr/bin/env python3
"""Generates a list from an async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Import async_generator from the previous task
    write a coroutine called async_comprehension that takes no arguments.
    Coroutine will collects 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    return [_ async for _ in async_generator()]
