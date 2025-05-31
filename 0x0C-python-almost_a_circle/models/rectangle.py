"""
A module to create the class rectangle and describe inheritance
"""

from models.base import Base


class Rectangle(Base):
    """ the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The initializer for the class
        Args:
            width: the width of the class
            height: the height of the class
            x: a parameter default 0
            y: a parameter default 0
            id: the id of the class assigned from the base class
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ the getter for the width private attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """The setter for the width private attribute"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """The getter for the height private attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """The setter for the height private attribute"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """the getter for the x private attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """the setter for the x private attribute"""

        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The getter for the y private attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """the setter for the y private attribute"""

        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        A method to get the area of the rectangle
        """

        return self.__height * self.__width

    def display(self):
        """
        A method to print the rectangle using a character
        """

        for _ in range(self.y):
            print('')
        for _ in range(self.__height):
            for _ in range(self.__x):
                print(' ', end="")
            for _ in range(self.__width):
                print("#", end="")
            print('')

    def __str__(self):
        """The override for the print method for the rectangle
        """

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y,
            self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """
        A methon to update the figures in a rectangle
        """

        # Define the attributes to be updated
        attribute_order = ["id", "width", "height", "x", "y"]

        for a in range(len(args)):
            setattr(self, attribute_order[a], args[a])
        if len(args) > 0:
            return
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """To create a dictionary representation of the class"""

        my_dict = {
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height
        }
        return my_dict
