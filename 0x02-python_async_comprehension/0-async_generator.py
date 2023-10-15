#!/usr/bin/env python3
"""
This module defines the `async_generator` coroutine. The coroutine loops
10 times, each time asynchronously waiting 1 second, then yields a random
number between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    This coroutine loops 10 times, each time asynchronously waiting 1
    second, then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
