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
    """Asynchronously generates 10 random numbers between 0 and 10, 
    waiting 1 second between each yield.
    
    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

