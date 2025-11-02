#!/usr/bin/env python3
""" a script to run some concurrent async coroutines"""

import asyncio

task_wait_random = __import__("3-tasks").wait_random

async def task_wait_n(n, max_delay):
    """ a function to spawn a couroutine for a specified time"""

    my_list = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
    return my_list