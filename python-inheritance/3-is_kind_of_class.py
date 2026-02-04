#!/usr/bin/python3
"""Module that defines a function to check if an object is an instance
 of a class or its subclass."""


def is_kind_of_class(obj, a_class):
    """Function that returns True if the object is an instance of, or if the
      object is an instance of a class that inherided from the specified class;
      otherwise False."""
    if isinstance(obj, a_class):
        return True
    else:
        return False
