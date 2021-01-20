#!/usr/bin/python3
""" this is Module Append to a file"""


def append_write(filename="", text=""):
    """Function that appends s tring at the end of a text file
    Return: the number of character added
    """
    with open(filename, mode='a', encoding='utf-8') as myfile:
        myfile.write(text)
        return myfile.tell()
