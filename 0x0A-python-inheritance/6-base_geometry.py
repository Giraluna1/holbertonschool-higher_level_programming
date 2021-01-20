#!/usr/bin/python3
""" Module Improve Geometry """


class BaseGeometry():
    """ Base Geometry class have:
    Method Area: that raise an exception
    """

    def area(self):
        """ Public method that raise an Exception """
        raise Exception('area() is not implemented')
