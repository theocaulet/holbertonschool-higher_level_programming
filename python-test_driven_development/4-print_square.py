#!/usr/bin/python3
"""Function that prints a square with the character #."""

def print_square(size):
    """
    Print a square with the character #.

    Args:
    size: size of the square.
    Raises:
    TypeError: if size is not an integer.
    TypeError: if size is a float and is less than 0.
    ValueError: if size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
