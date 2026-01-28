#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square with a given size."""
    def __init__(self, size=0):
        """Initialize a Square instance with size validation."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
