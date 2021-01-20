#!/usr/bin/python3
""" Module Rectangle """

class BaseGeometry():
    """ Base Geometry class have:
    Method Area: that raise an exception
    Methoss integer validator: that validates values
    """

    def area(self):
        """ Public method that raise an Exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ Public method that validates value
            if the value is not a integer: raise Type Error
            if the value is less or equal to 0: raise a Value Error
        """
        self.value = value
        self.name = name
        if type(self.value) is not int:
            raise TypeError('{} must be an integer'.format(self.name))
        if self.value <= 0:
            raise ValueError('{} must be greater than 0'.format(self.name))

class Rectangle(BaseGeometry):
""" class that inherits from BaseGeomety """

    __width = 0
    __height = 0

    def __init__(self, width, height):
        """ instantation """
        self.__width = width
        self.__height = height

        if integer_validator(width, s)

