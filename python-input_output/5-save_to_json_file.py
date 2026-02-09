#!/usr/bin/python3
import json
"""Function that writes an object to a text file,
 using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """Define a save_to_json_file function."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
