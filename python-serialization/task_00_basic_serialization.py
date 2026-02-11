#!/usr/bin/python3
"""Function that serializes an object to a file
 and deserializes an object from a file."""
import json


def serialize_and_save_to_file(data, filename):
    """Define a serialize_and_save_to_file function."""
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Define a load_and_deserialize function."""
    with open(filename, 'r') as file:
        return json.load(file)
