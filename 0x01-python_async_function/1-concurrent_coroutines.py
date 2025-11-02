#!/usr/bin/env python3
""" a script to run some concurrent async coroutines"""

import asyncio

wait_random = __import__("0-basic_async_syntax").wait_random

async def wait_n(n, max_delay):
    """ a function to spawn a couroutine for a specified time"""

    my_list = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return my_list