#!/usr/bin/python3
""" Module SAve Object to a file"""

import json


def save_to_json_file(my_obj, filename):
    """ Function that writes an Object to a text file,
    using a JSON representation
    """
    with open(filename, mode='w', encoding='utf-8') as text_file:
        print(text_file.write(json.dumps(my_obj)), end='')
