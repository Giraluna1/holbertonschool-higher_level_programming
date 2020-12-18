#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # ordenamos el diccionario en lista de tuplas
    dicty = sorted(a_dictionary.keys())
    for item in dicty:
        print('{}: {}'.format(item, a_dictionary[item]))
