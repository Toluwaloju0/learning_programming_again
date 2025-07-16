#!/usr/bin/env python3
""" a module to define a function to divide a matrix"""

def matrix_divided(matrix, div):
    """ a function to divide a matrix by a divisor
    Args:
        matrix (list of list): the matrix to be divided
        div (int): the divisor
    return: a new matrix with the divided values
    """

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # create a new list to store the divided values of the list
    new_matrix = []

    for a in range(len(matrix)):
        if not isinstance(matrix[a], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[a]) != len(matrix[0]):
            raise TypeError(" Each row of the matrix must have the same size")
        new_matrix.append([])
        # iterate over the matrix and check if it has only int or floats
        for b in range(len(matrix[a])):
            if not isinstance(matrix[a][b], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[a].append(round(float(matrix[a][b]) / div, 2))

    return new_matrix
