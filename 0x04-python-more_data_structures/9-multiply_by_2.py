#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dicty = sorted(a_dictionary.keys())
    return (dict(map(lambda item: a_dictionary[item] * 2, dicty)))