#!/usr/bin/python3
""" Module Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class that inherits from BaseGeomety """

    def __init__(self, width, height):
        """ instantation constructor
        Args:
        width (int): width of a rectangle
        height (int): height of a rectangle

        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
