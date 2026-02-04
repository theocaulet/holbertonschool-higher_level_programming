#!/usr/bin/python3
"""Define an abstract base class Shape with area and perimeter methods."""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Create a Shape class."""
    @abstractmethod
    def area(self):
        """Define the area method."""
        pass

    @abstractmethod
    def perimeter(self):
        """Define the perimeter method."""
        pass


class Circle(Shape):
    """Create a Circle class that inherits from Shape."""
    def __init__(self, radius):
        """Initialize the circle with a radius."""
        self.radius = radius

    def area(self):
        """Define the area of the circle."""
        PI = 3.14159
        return PI * (self.radius * self.radius)

    def perimeter(self):
        """Define the perimeter of the circle."""
        PI = 3.14159
        return 2 * PI * self.radius


class Rectangle(Shape):
    """Create a Rectangle class that inherits from Shape."""
    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Define the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Define the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(Shape):
    """Define a function that take a single argument."""
    print(f"Area: {Shape.area()}")
    print(f"Perimeter: {Shape.perimeter()}")
