#!/bin/usr/python3
""" Module Lookup """


def lookup(obj):
    """ Function
    Args:
        obj: Object
    Return: the list of available attributes and methods of an object
    """
    return (dir(obj))
