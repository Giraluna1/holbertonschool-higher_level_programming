#!/usr/bin/python3
"""
This is he module Print square

"""


def print_square(size):
    """
    Function that print a Square
    Args:
        size (int): is the size length of the square
    """
    if type(size) is int:
        if size < 0:
            raise ValueError('size must be >= 0')
        if size == 0:
            pass

        for i in range(size):
            for i in range(size):
                print('#', end='')
            print()
    else:
        raise TypeError('size must be an integer')
