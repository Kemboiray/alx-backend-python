#!/usr/bin/env python3
"""This module defines an async coroutine `wait_n`"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `wait_random` `n` times with specified `max_delay`

    Returns: List of delays in ascending order
    """
    return sorted(
        list(await
             asyncio.gather(*(wait_random(max_delay) for _ in range(n)))))
