#!/usr/bin/env python3
""" a module to create a function which converts a float to a string"""

def to_str(n: float) -> str:
    """ a function to convert a float to a string
    Args:
        n: the float number to be converted
    Return: the string containing the number
    """

    return "{}".format(n)