#!/usr/bin/python3
""" This is module Exact same Object """


def is_same_class(obj, a_class):
    """ Function check is the same class
    Args:
        obj (int): object
        a_class (objec): (wherever you want): any class
    Return:
        True if the object is exactly an instance
    """
    if type(obj) == a_class:
        return True
    else:
        return False
