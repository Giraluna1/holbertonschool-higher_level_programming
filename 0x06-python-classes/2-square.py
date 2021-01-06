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
        """ __init method.
        Args:
            size (int): size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be a integer")
        elif size < 0:
            raise ValueError("size mut be >= 0")
        else:
            self.__size = size
