#!/usr/bin/env python3
"""This module defines an async coroutine `task_wait_n`"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `task_wait_random` `n` times with specified `max_delay`

    Returns: List of delays in ascending order
    """
    return sorted(
        list(await
             asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))))
