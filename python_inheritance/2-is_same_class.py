#!/usr/bin/python3
"""
A function to check if an obj is an instance of a class
"""

def is_same_class(obj, a_class):
    """
    The function to check if the object is an instance of the class
    Args:
        obj: The object to be checked
        a_class: the class to be tested against

    """
    return isclass(obj, a_class)