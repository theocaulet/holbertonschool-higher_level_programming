#!/usr/bin/python3
"""Function that writes an object to a text file,
 using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """Define a save_to_json_file function."""
    import json
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
