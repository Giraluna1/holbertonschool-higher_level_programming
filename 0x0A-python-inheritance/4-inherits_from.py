#!/bin/usr/python3
""" This is the Module Only sub class of """


def inherits_from(obj, a_class):
    """ Function that checks if the object is an
        instance of a class that inherited (directly o indirectly)
        from the specified class
    Args:
        obj (bool): object type bool
        a_class (wherever type): any class
    Return: True o false
    """
    if type(obj) is a_class:
            return False
    if issubclass(type(obj), a_class):
        return True
    else:
        return False
