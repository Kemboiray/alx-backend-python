#!/usr/bin/env python3
"""
This module defines a coroutine, `measure_runtime` that executes
`async_comprehension` four times in parallel and returns the total run time
"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of `async_comprehension` """
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - s
