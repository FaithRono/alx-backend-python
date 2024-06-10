#!/usr/bin/env python3

''' Description: Import wait_random from the previous python file that
                 you’ve written and write an async routine called wait_n
                 that takes in 2 int arguments: max_delay and n. You will
                 spawn wait_random n times with the specified max_delay.

                 wait_n should return the list of all the delays (float values).
                 The list of the delays should be in ascending order without
                 using sort() because of concurrency.
    Arguments: n: int, max_delay: int = 10
'''

import asyncio  # Import asyncio for handling asynchronous operations
import random   # Import random to generate random numbers
from typing import List  # Import List for type hinting

# Import the wait_random coroutine from the previous file
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waits for random delay until max_delay, returns list of actual delays """
    
    spawn_ls = []  # List to hold the spawned asyncio tasks
    delay_ls = []  # List to hold the actual delays

    # Loop to create n tasks
    for i in range(n):
        # Create a new task for wait_random with max_delay
        delayed_task = asyncio.create_task(wait_random(max_delay))
        # Add a callback to append the result of the task to delay_ls
        delayed_task.add_done_callback(lambda x: delay_ls.append(x.result()))
        # Append the created task to the spawn_ls list
        spawn_ls.append(delayed_task)

    # Wait for all tasks to complete
    for spawn in spawn_ls:
        await spawn

    # Return the list of delays
    return delay_ls
