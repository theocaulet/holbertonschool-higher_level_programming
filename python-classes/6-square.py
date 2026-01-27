#!/usr/bin/python3
"""Defines a Square class"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance with size and position.
        Args:
        size(int): The size of the square
        position(tuple): The position of the square
        """
        self.size = size
        self.position = position

    def area(self):
        """Define the current Square area."""
        return self.size * self.size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Print the square with the # character."""
        if self.size == 0:
            print()
        else:
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
        if self.position[1] > 0:
            for _ in range(self.position[1]):
                print()

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple"
                            " of 2 positive integers")
        for element in value:
            if not isinstance(element, int) or element < 0:
                raise TypeError("position must be a tuple"
                                " of 2 positive integers")
            self.__position = value
