#!/usr/bin/python3
""" Module From JSON string to Object """

import json


def from_json_string(my_str):
    """ Function that Returns an object (python D.S)
    represented by json string
    """
    return (json.loads(my_str))
