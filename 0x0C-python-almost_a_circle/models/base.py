#!/usr/bin/python3
""" Module Base class """


import json


class Base:
    """ The principal Class Base
    Private attribute:
        __nb_objects
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor
        Args: id (int): identification number
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ method that return the JSON string representation """
        if list_dictionaries is None:
            return '[]'
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ method that writes the json string representation of list of objects
            to a file
        """
        filename = cls.__name__

        if list_objs is None:
            list_objs = []

        list_dicti = []
        for obj in list_objs:
            list_dicti.append(obj.to_dictionary())

        my_json_string = cls.to_json_string(list_dicti)

        with open(filename+'.json', mode='w', encoding='utf-8') as file:
            file.write(my_json_string)

    @staticmethod
    def from_json_string(json_string):
        """This method returns the list of the JSON string representation """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ class method that returns an instance with all
            attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(width=6, height=4)
        elif cls.__name__ == 'Square':
            dummy = cls(size=7)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances"""
        filename = cls.__name__

        list_objs = []

        try:
            with open(filename+'.json', encoding='utf-8') as file:
                list_dicti = cls.from_json_string(file.read())
                for dicti in list_dicti:
                    list_objs.append(cls.create(**dicti))
                return list_objs
        except Exception:
            return []



