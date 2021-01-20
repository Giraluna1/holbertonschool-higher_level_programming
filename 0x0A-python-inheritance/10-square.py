#!/usr/bin/python3
""" Module Square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class that inherits from Rectangle """

    def __init__(self, size):
        """ Constructor instantiation
        Args:
            size(int) =  size of the square
        """
        self.__size = size
        self.integer_validator("size", size)

        super().__init__(size, size)

s = Square(13)

print(s)
print(s.area())
