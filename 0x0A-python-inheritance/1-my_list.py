#!/usr/bin/python3
""" This is the Module My list """


class MyList(list):
    """ inherits from list class
    """

    def print_sorted(self):
        """Method that prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
