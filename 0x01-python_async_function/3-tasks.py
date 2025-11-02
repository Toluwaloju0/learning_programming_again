#!/usr/bin/env python3
""" a script to create a task"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random

def task_wait_random(max_delay):
    """ a function to create a asyncio task
    Args:
        max_delay: the interger to be given to the wait_random function
    """

    return asyncio.create_task(wait_random(max_delay))