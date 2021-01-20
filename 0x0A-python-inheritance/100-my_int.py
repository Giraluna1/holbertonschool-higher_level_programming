#!/usr/bin/python3
"""This is the module My integer """


class MyInt(int):
    """ Class inheritance from int"""

    def __eq__(self, number):
        """checks for equality beetwen two MyInts
        return False o True
        """
        return int(self) != number

    def __ne__(self, number):
        """checks for equality beetwen two MyInts
        return: True o False
        """
        return int(self) == number
