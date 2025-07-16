#!/usr/bin/python3
""" a  module to print a string based on indentation"""

def text_indentation(text):
    """ A function to print a string by breaking it at indents
    Args:
        text (string): the string to be printed
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    string = ""

    for char in text:
        string += char
        if char == ',' or char == '.' or char == ':' or char == "?":
            a = 0
            for new_char in string:
                if new_char != ' ':
                    break
                a += 1
            print(f'{string[a:]}\n')
            string = ''

    a = 0
    for new_char in string:
        if new_char != ' ':
            break
        a += 1
    print(string[a:])
