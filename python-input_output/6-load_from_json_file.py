#!/usr/bin/python3
import json
"""Function that creates an object from a "JSON file"."""


def load_from_json_file(filename):
    """Define a load_from_json_file function."""
    with open(filename, 'r') as file:
        return json.load(file)
