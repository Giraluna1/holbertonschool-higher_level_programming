#!/usr/bin/python3
""" This is module Rectangle Class"""


class Rectangle():
    """ Class Rectangle """

    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """ Constructor
        Args:
            width (int): width of Rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve it """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value: width of Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ retrieve it """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value: height of Rectangle
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
