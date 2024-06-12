#!/usr/bin/env python3
"""
coroutine async_generator taking no args
loops 10 times each time asynchronously wait 1 second
then yield a random number between 0 and 10.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Async comprehension generator"""
    tasks = [asyncio.sleep(1) for _ in range(10)]
    await asyncio.gather(*tasks)
    for _ in range(10):
        yield random.uniform(0, 10)
