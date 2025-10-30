#!/usr/bin/python3
""" a module to create a function which returns a tuple of the arguments passed"""

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ a function to create a tuple of the arguments passed
    Args:
        k: the string to be used in the tuple
        v: a float of int value to be used in the tuple
    Return: a tuple containing the passed arguments
    """
    
    return (k, float(v ** 2))