#!/usr/bin/python3
"""Module that defines a function to check class of an object."""


def is_same_class(obj, a_class):
    """Function that returns True if the object is exactly
      an instance of the specified class; otherwise False."""
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
