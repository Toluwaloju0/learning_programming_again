#!/usr/bin/env python3
""" a script to create a coroutine function"""

import asyncio
from random import uniform

async def wait_random(max_delay=10):
    """ a function which is a courotine delaying for 10 seconds
    Args:
        max_delay: the delay time 
    """

    sleep = uniform(0, max_delay)

    await asyncio.sleep(sleep)
    return sleep