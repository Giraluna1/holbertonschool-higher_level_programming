#!/usr/bin/python3
""" This is the module the pick number"""


def find_peak(list_of_integers):
    """ find_peak recive list of int"""
    if not list_of_integers:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
