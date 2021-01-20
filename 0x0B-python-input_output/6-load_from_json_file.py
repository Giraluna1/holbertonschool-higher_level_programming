#!/usr/bin/python3
""" Module Create object from a JSON file"""

import json


def load_from_json_file(filename):
    """ Function that creates an Object from "JSON FILe"""

    with open(filename, mode='r', encoding='utf-8') as text_file:
        return json.load(text_file)
