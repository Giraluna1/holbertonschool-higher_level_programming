#!/usr/bin/python3
""" Module Write to a file """


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    Return: number od characters written
    """
    with open(filename, mode='w', encoding='utf-8') as myfile:
        myfile.write(text)
        return myfile.tell()
