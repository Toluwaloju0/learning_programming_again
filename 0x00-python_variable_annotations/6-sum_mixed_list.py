#!/usr/bin/env python3
""" a module to create a function which adds the intergers and floats in a string"""

from typing import List, Union

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ a function to sum the content of a list 
    Args:
        mxd_list: the list containing floats and intergers to be added
    Returns: the sum of all the content in the list
    """

    sum: float = 0
    
    for x in mxd_list:
        sum += x

    return sum