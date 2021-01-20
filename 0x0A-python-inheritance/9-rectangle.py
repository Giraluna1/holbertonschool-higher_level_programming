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

    def area(self):
        """ return: the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return: an print rectangle description:
            [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
