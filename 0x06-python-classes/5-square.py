#!/usr/bin/python3
""" Square Class documentation

 """


class Square():
    """  Size of Square.

    Private instance attribute:
        __size
    Instantiation with size (no type/value verification).

    """
    __size = None

    def __init__(self, size=0):
        """ __init method size.
        Args:
            size (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """obtain size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set the value.
        Args:
            value : value of the size of the square.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ method area.
        Args:
            None
        Return:
            Area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """ method print square
        Return:
            figure square with the character #
        """
        if self.__size is 0:
            print()
        for i in range(self.__size):
            for i in range(self.__size):
                print('#', end='')                
            print()
