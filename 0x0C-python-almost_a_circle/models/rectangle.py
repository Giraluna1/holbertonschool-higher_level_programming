#!/usr/bin/python3
""" Module Rectangle """

from models.base import Base


class Rectangle(Base):
    """ class rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ constructor
        Args:
            width (int): width of a rectangle
            height (int):height of a rectangle
            x
            y
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def x(self):
        """ x position """
        return self.__x

    @x.setter
    def x(self, value):
        """Args:
        x: position on x vector
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """ y vector """
        return self.__y

    @y.setter
    def y(self, value):
        """Args:
            y: position on y vector
        """
        if value < 0:
            raise ValueError('y must be >= 0')
        elif not isinstance(value, int):
            raise TypeError('y must be an integer')
        else:
            self.__y = value

    def area(self):
        """ method area
        Return: the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """ display the figure
        Return: the figure of the Rectangle in #
        """

        for i in range(self.__y):
            print()
        row = ('{}{}'.format((self.__x * ' '), (self.__width * '#')))
        for i in range(self.__height):
            print(row)

    def __str__(self):
        """return: an print rectangle description:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ method that assigns a key/value argument to attributes: """

        attr = ['id', 'width', 'height', 'x', 'y']
        if len(args) > 0:
            for arg in range(len(args)):
                setattr(self, attr[arg], args[arg])
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ the dictionary representation of a Rectangle """
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
