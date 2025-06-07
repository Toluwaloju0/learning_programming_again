#!/usr/bin/python3
"""
A module to create a new class inheriting from list
"""

class MyList(list):
    """The class inheriting from list
    """
    def print_sorted(self):
        """A method to print the members of the list in sorted form
        """

        print(sorted(self))
