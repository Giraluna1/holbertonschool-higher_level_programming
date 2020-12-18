#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dicty = {}
    dicty = sorted(a_dictionary.keys())
    for item in dicty:
        new_dicty[item] = a_dictionary[item] * 2
    return new_dicty