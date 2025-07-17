#!/usr/bin/python3
""" a module to create a locked class which allows setting specific attributes"""

class LockedClass:
    """ a class which allows only specific attributes to be set"""

    __slots__ = ["first_name"]
    pass