#!/usr/bin/python3
"""Module that defines a class BaseGeometry, Rectangle and Square."""


class BaseGeometry:
    """Create a class BaseGeometry"""
    def area(self):
        """Public instance method that raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value."""
        if isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Create a class Rectangle that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height


class Square(Rectangle):
    """Create a class Square that inherits from Rectangle."""
    def __init__(self, size):
        """Initialize size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the Square."""
        return self.__size * self.__size
