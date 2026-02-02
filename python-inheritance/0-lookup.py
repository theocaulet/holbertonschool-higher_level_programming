#!/usr/bin/python3
def lookup(obj):
    """Return the list of attributes and methods of an object."""
    return list(dir(obj))
