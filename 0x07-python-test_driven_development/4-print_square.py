#!/usr/bin/python3
""" a module to print a square using #"""

def print_square(size):
    """ a function to print a square
    Args:
        size (int): the size of the square to be printed
    """

    if not isinstance(size, (int)):
        raise TypeError("size must be an integer")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print('')
