#!/usr/bin/env python3

''' Description: Take the code from wait_n and alter it into a new function
                 task_wait_n. The code is nearly identical to wait_n except
                 task_wait_random is being called.
    Arguments: n: int, max_delay: int = 10
'''

from typing import List  # Import List for type hinting
import asyncio  # Import asyncio for handling asynchronous operations
import random  # Import random to generate random numbers

# Import the task_wait_random coroutine from the 3-tasks module
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Execute task_wait_random and returns sorted list of delay'''
    spawn_ls = []  # List to hold the spawned asyncio tasks
    delay_ls = []  # List to hold the actual delays

    # Loop to create n tasks
    for i in range(n):
        # Create a new task for task_wait_random with max_delay
        delayed_task = task_wait_random(max_delay)
        # Add a callback to append the result of the task to delay_ls
        delayed_task.add_done_callback(lambda x: delay_ls.append(x.result()))
        # Append the created task to the spawn_ls list
        spawn_ls.append(delayed_task)

    # Wait for all tasks to complete
    for spawn in spawn_ls:
        await spawn

    # Return the sorted list of delays
    return sorted(delay_ls)
