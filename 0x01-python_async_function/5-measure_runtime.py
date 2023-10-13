#!/usr/bin/env python3
"""This module defines the function `measure_time`"""

import time
import asyncio

task_wait_n = __import__("4-tasks").task_wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the total execution time for task_wait_n(n, max_delay)"""
    s = time.perf_counter()
    asyncio.run(task_wait_n(n, max_delay))
    return (time.perf_counter() - s) / n
