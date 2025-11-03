#!/usr/bin/env python3
""" a script to create a class which implements redis"""

import redis
import uuid

from typing import Any, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """ a method to count hw many times keys in redis are called"""

    @wraps(method)
    def incr(self, data: str):
        """ a function to get the value of a key and return that value using the appopraite function"""

        self._redis.incr(method.__qualname__)
        return method(self, data)

    return incr

def call_history(method: Callable) -> Callable:
    """ a decorator to save and get list of calls made"""

    @wraps(method)
    def history(self, data):
        """ the function to be returned from the decorator"""

        self._redis.rpush('{}:inputs'.format(method.__qualname__), data)

        key = method(self, data)
        self._redis.rpush("{}:outputs".format(method.__qualname__), key)

        return key

    return history

def replay(method: Callable):
    """ a replay function for the classes"""

    r = redis.Redis()
    return int(r.get(method.__qualname__))

class Cache:
    """ the class implementing redis """

    def __init__(self):
        """ the init of the redis class"""

        self._redis = redis.Redis()

        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Any) -> str:
        """ a function to store data into the redis client
        Args:
            data: the data to be inserted into the database
        Return a string which is the key to the data in the database
        """

        key = str(uuid.uuid4())

        self._redis.set(key, data)
        return key

    def get(self, key:str, fn: Callable=None):
        """ a method to get the data stored in a key"""

        data = self._redis.get(key)

        return fn(data) if data is not None and fn is not None else data