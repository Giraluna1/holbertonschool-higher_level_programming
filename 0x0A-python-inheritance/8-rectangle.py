#!/usr/bin/python3
""" Module Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class that inherits from BaseGeomety """

    __width = 0
    __height = 0

    def __init__(self, width, height):
        """ instantation constructor
        Args:
        width (int): width of a rectangle
        height (int): height of a rectangle

        """
        BaseGeometry.integer_validator(self, "width", width)
        self.__width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height
