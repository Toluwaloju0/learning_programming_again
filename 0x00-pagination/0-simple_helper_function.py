#!/usr/bin/env python3
""" a function to get the objects to be used when quering a list item"""

def index_range(page, page_size):
    """ a function to get the index of items to be accessed from a page
    Args:
        page: a number to to get tthe start page
        page_size: a number to show how many items should be in a page
    return a tuple containing the start and end items of a page
    """

    return (((page - 1) * page_size), (page * page_size))