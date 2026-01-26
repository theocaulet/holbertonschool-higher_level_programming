#!/usr/bin/python3
"""Define a class Square with private attribute size and value checks."""


class Square:
    def __init__(self, size=0):
        self.size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
