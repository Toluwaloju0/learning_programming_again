#!/usr/bin/python3
""" a module to define a class called rectangle"""

class Rectangle:
    """ the rectangle class"""

    def __init__(self, width=0, height=0):
        """ the initializer for the class """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ the getter for the width private attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """ the setter for the width private attribute"""

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ the getter for the height private attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """ the setter for the height private attribute"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value