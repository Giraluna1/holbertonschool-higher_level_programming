#!/usr/bin/python3
""" Module Load, add, save """
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    object_json = load_from_json_file(filename)
except Exception:
    save_to_json_file((sys.argv[1:]), filename)
else:
    object_json += sys.argv[1:]
    save_to_json_file(object_json, filename)
