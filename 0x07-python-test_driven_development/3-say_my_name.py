#!/usr/bin/python3
""" This is Module Say my name"""


def say_my_name(first_name, last_name=""):
    """ This function print the full name
    Args:
        first_name (str): Name
        last_name (str): Last
    """
    if type(first_name) is str and type(last_name) is str:
        print('My name is {} {}'.format(first_name, last_name))
    else:
        if type(first_name) is not str:
            raise TypeError('first_name must be a string')
        elif type(last_name) is not str:
            raise TypeError('last_name must be a string')
