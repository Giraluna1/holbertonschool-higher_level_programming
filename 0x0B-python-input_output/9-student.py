#!/usr/bin/python3
""" Module Student to Json"""


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

    def to_json(self):
        """ retrieves a dictionary representation of
        a student instance
        """
        return self.__dict__
