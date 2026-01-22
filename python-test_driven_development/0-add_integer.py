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
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
