#!/usr/bin/python3
""" Module REad file """


def read_file(filename=""):
    """ Function that read a file """

    with open(filename, encoding='utf-8') as myfile:
        print(myfile.read())
