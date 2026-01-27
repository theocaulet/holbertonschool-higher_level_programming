#!/usr/bin/python3
"""Defines a Square class."""


class Square:
    def __init__(self, size=0):
        """Initialize a Square instance with size validation."""
        self.size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Define the current Square area."""
        return self.size * self.size
