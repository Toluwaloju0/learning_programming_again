#!/usr/bin/env python3
""" a function to get a page from the web"""

import requests
import redis

from functools import wraps

def decorator(method):
    """ a function to decorate the get_page function
    Args:
        method: the method to be decorated
    """

    @wraps(method)
    def count(url):
        r = redis.Redis()

        r.incr("count:{}".format(url))
        r.expire("count:{}".format(url), 10)

        method(url)

    return count

@decorator
def get_page(url: str) -> str:
    """ a function ot get a webpage and how many times it was accessed
    Args:
        url: the url to be accessed
    """

    res = requests.get(url)
    return res.text

get_page("http://slowwly.robertomurray.co.uk/")
