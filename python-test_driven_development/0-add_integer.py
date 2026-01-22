#!/usr/bin/python3
"""
Function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers and return the result.

    Args:
    a: first integer
    b: second integer

    Return:
    The sum of a and b

    Raises:
    TypeError: if a and b are not integers or floats
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
