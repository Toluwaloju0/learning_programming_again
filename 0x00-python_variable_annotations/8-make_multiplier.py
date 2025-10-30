#!/usr/bin/env python3
""" a module to create a function """

from typing import Callable

def make_multiplier(multiplier: float) -> Callable:
    """ a function to multiplier a float as multiplier
    Args:
        multiplier: the multiplier to multiply to float by
    Return a function which accepts a float that is multiplied by multiplier
    """

    def multiply(n: float) -> float:
        """ a function which accepts a float and multiply it
        Args:
            n: the float to be multiplied
        Returns the multiplication of the float by multiplier
        """

        return n * multiplier

    return multiply