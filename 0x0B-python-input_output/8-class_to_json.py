#!/usr/bin/python3
"""Module Class to JSON """


def class_to_json(obj):
    """ Function
    Args: obj : intance of a class
    Return: the dictionary description
    """
    return obj.__dict__
