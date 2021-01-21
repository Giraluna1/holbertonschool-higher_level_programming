#!/usr/bin/python3
""" Module Student to Json with filter """


class Student:
    """ class that defines a student """

    def __init__(self, first_name, last_name, age):
        """ Constructor
        Args:
            first_name (str): first name of a student
            last_name (str):last name of student
            age (int): age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self. age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation of
        a student instance
        """
        if type(attrs) is not list:
            return self.__dict__
        else:
            return dict((_key, self.__dict__[_key])
                        for _key in attrs if _key in self.__dict__)

    def reload_from_json(self, json):
        """ replaces all atributes of the Student instance """
        for key in json:
            setattr(self, key, json[key])
