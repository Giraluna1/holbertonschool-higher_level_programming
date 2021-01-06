#!/usr/bin/python3
""" Square Class documentation

Attributes:
    size and position

"""


class Square():
    """  Size of Square.

    Private instance attribute:
        __size : size of square
        __position:

    """
    __size = None
    __position = None

    def __init__(self, size=0, position=(0, 0)):
        """ __init method size.
        Args:
            size (int): size of the square.
            position (int): coordinates of where the square is located.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """obtain size of square acording the value"""
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

    @property
    def position(self):
        """obtain where is the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """ set the value.
        Args:
            value : are two positive integers.
        """
        if (type(value) is not tuple) or type(value[0]) is not int or\
            not isinstance(value[1], int) or (len(value) is not 2) or\
                (value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ method area.
        Args:
            None
        Return:
            Area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """ method print square.
        Return:
            figure square with the character #
        """
        if self.__size is 0:
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for i in range(self.__size + self.__position[0]):
                if i < self.__position[0]:
                    print(' ', end='')
                else:
                    print('#', end='')
            print()
