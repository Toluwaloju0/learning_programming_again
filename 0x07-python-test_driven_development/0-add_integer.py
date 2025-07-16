#!/usr/bin/env python3
""" a module to define an add integer function"""


def add_integer(a, b=98):
    """ a function to add two integers toghether
    Args:
        a (int): the first integer
        b (int): the second integer default value is 98
    Return: the added value of a and b
    """

    # check if the values given are integers or floats
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # cast a and b to integers and return the addition
    return int(a) + int(b)
