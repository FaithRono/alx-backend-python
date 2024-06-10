#!/usr/bin/env python3


# 0-basic_async_syntax.py
import asyncio  # Import the asyncio module to handle asynchronous operations
import random   # Import the random module to generate random numbers

# Define an asynchronous coroutine named wait_random
# This coroutine takes an integer argument max_delay with a default value of 10
# It waits for a random delay between 0 and max_delay seconds and eventually
# returns the delay


async def wait_random(max_delay: int = 10) -> float:
    # Generate a random float between 0 and max_delay
    delay = random.uniform(0, max_delay)
    # Pause the coroutine for the generated delay time
    await asyncio.sleep(delay)
    # Return the delay
    return delay
