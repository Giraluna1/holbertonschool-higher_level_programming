#!/usr/bin/python3
""" Module Square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ class that inherits from Rectangle """

    def __init__(self, size, x=0, y=0, id=None):
        """ Constructor instantiation
        Args:
            size(int) =  size of the square
            x (int)= vector x position
            y (int)= vector y position
            id (int) = number identification
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, size):
        """ set for size """
        self.width = size
        self.height = size

    def __str__(self):
        """return: an print rectangle description:
            [Square] (<id>) <x>/<y> - <size>
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ update that assigns attributes """
        attr = ['id', 'size', 'x', 'y']
        if len(args) > 0:
            for arg in range(len(args)):
                setattr(self, attr[arg], args[arg])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key)
                    setattr(self, key, value)

    def to_dictionary(self):
        """ the dictionary representation of a Rectangle """
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
