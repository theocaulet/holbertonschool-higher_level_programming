#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""


class BaseGeometry:
    """Create a class BaseGeometry"""
    def area(self):
        """Public instance method that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Create a class Rectangle that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize width and height."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
