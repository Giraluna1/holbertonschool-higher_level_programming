#!/usr/bin/python3
""" This is the module Divide a matrix"""


def matrix_divided(matrix, div):
    """
    This function divide a matrix by div rounded two decimals
    Args:
        matrix (list): list of lists of integers or floats
        div (int): can´t be equal to 0
    """
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div is 0:
        raise ZeroDivisionError("division by zero")

    rows_1 = len(matrix)
    new_matrix = []

    for i in matrix:
        for element in i:
            if not isinstance(element, (int, float)):
                raise TypeError('matrix must be a matrix '
                                '(list of lists) of integers/floats')
        if not isinstance(i, list):
            raise TypeError('matrix must be a matrix (list of lists) '
                            'of integers/floats')
        else:
            new_matrix.append(list(map(lambda x: round(x / div, 2), i)))

    rows_2 = len(new_matrix)

    if rows_2 != rows_1:
        raise TypeError('Each row of the matrix must have the same size')

    return new_matrix
