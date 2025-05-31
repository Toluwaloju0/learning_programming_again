#!/usr/bin/pyrhon3
"""
A module to create a square class that inherits from rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class that inherits from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        The initializer for the square class
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The print function for the square class
        which overides that of the rectangle class"""

        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self):
        """The getter for the size attribute"""

        return self.height

    @size.setter
    def size(self, value):
        """
        The setter for the size variable
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """The function to update the square class"""

        attribute_list = ["id", "size", "x", "y"]
        for a in range(len(args)):
            setattr(self, attribute_list[a], args[a])
        if len(args) > 0:
            return
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """To create a dictionary representation of the square class"""

        my_dict = {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "size": self.size
        }
        return my_dict
