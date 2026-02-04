#!/usr/bin/python3
"""Module that defines a function to lookup
 attributes and methods of an object."""


def lookup(obj):
    """Return the list of attributes and methods of an object."""
    return list(dir(obj))
