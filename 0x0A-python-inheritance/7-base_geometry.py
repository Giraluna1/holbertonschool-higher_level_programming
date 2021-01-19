#!/bin/usr/python3
""" Module Integer validator """


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
