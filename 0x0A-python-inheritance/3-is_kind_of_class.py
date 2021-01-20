#!/usr/bin/python3
""" This is the mode Same class or inherit from """


def is_kind_of_class(obj, a_class):
    """function that check is inherited class
    Args:
        obj (int): object type integer
        a_class (wherever type): any class
    Return:
        bool: True o False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
