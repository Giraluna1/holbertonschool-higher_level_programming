#!/usr/bin/python3
"""
This is he module Integers addition

"""


def add_integer(a, b=98):
    """ Is a Function add only two integers """
    if type(a) is int or type(a) is float:
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if type(b) is int or type(b) is float:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return (a + b)
