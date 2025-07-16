#!/usr/bin/python3
""" a module to print a persons name"""

def say_my_name(first_name, last_name=""):
    """ a function to print a persons name
    Args:
        first_name (str): the persons first name
        last_name (str): the persons last name default is null

    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")