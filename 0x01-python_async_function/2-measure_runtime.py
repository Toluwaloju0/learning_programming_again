#!/usr/bin/env python3
""" a module to create a function whic measures the runtime of a async function"""

import time
import asyncio

wait_n = __import__("1-concurrent_coroutines").wait_n

def measure_time(n, max_delay):
    """ a function to measure the runtime of a async function"""

    start = time.time()

    asyncio.run(wait_n(n, max_delay))

    return (time.time() - start) / n