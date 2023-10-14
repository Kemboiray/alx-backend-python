#!/usr/bin/env python3
"""
This module defines a coroutine, `async_comprehension` that comprehenses
over an async generator and collects values to return
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Comprehense over an async generator and collect values to return """
    return [i async for i in async_generator()]
