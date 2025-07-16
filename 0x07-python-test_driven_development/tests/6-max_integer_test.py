#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest


max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ a class to hold test functions for the max_integer function"""

    def test_max_interger(self):
        """ the method to assert that the max integer function
        works correctly"""

        self.assertEqual(max_integer([1, 3, 5, 9, 3, 6]), 9, "Max integer does not work correctly")
        self.assertNotEqual(max_integer([1, 3, 5, 9, 3, 6]), 7, "Max integer does not work correctly")
        self.assertEqual(max_integer([]), None, "Max integer does not work correctly")
