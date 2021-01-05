#!/usr/bin/python3
""" Square Class that based 0-square.py.

 """


class Square():
    """ An define Size of Square.

    Private instance attribute:
        __size
    Instantiation with size (no type/value verification).

    """
    __size = None

    def __init__(self, size=None):
        """ __init method.
        Args:
            size : None size of square.
        """
        self.__size = size  #: private instance
