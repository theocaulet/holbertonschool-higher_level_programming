#!/usr/bin/python3
import pickle
"""Function that serializes an object to a file
 and deserializes an object from a file."""


def serialize_and_save_to_file(data, filename):
    """Define a serialize_and_save_to_file function."""
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    """Define a load_and_deserialize function."""
    with open(filename, 'rb') as file:
        return pickle.load(file)
