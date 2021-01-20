#!/usr/bin/python3
""" This is the Module My list """


class Mylist(list):
    """ inherits from list class """

    def print_sorted(self):
        """Method that prints the list, but sorted (ascending sort)
        """
        List_sorted = sorted(self)
        print(List_sorted)
