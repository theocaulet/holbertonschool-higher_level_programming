#!/usr/bin/python3
"""Define the BaseGeometry class and its validation helpers."""


class BaseGeometry:
    """Base class for geometry objects with validation utilities."""
    def area(self):
        """Raise an exception because area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that `value` is a positive integer.

        Args:
            name (str): The parameter name used in error messages.
            value (int): The value to validate.

        Raises:
            TypeError: If `value` is not an integer or is a boolean.
            ValueError: If `value` is less than or equal to zero.
        """
        if not isinstance(value, int) or not isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
