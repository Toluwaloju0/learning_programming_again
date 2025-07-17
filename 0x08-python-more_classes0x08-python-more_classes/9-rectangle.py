#!/usr/bin/python3
""" a module to define a class called rectangle"""

class Rectangle:
    """ the rectangle class"""

    number_of_instances = 0  # to record the number of instances the class is created
    print_symbol = "#"  # the symbol to used to print the class

    def __init__(self, width=0, height=0):
        """ the initializer for the class """

        self.width = width
        self.height = height
        # increment number of instances by 1
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ a method to get the area of the rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """ a function to get the perimeter of the rectangle"""

        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ a method to set what to print when printing the string"""

        rectangle_string = ''
        for _ in range(self.__height):
            for _ in range(self.__width):
                rectangle_string +=  str(self.print_symbol)
            rectangle_string += '\n'

        return rectangle_string[:-1]

    def __repr__(self):
        """ a method to edit a rectangle print out"""

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ a method to delete the class instance"""

        print("Bye rectangle...")
        # decrease the number of instances by 1
        Rectangle.number_of_instances -= 1
        del self

    @staticmethod
    def  bigger_or_equal(rect_1, rect_2):
        """ a static class method to get the biggests rectangle
        Args:
            rect_1 (Rectangle): the first rectangle
            rect_2 (Rectangle): the second rectangle
        Return: the biggest rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ a method to create a square from an instance of a Rectangle"""

        square = cls(size, size)
        
        return square