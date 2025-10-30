#1/usr/bin/env python3
""" a module to create a function which accepts a list of floats"""

from typing import Iterable
def sum_list(input_list: Iterable[float]) -> float:
    """a function to add the values of a list together
    Args:
        input_list: the list containing floats to be added
    Return: a float which is the sum of all the values in the list
    """

    sum: float = 0
    for x in input_list:
        sum += x

    return sum