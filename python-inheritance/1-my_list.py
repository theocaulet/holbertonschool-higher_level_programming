#!/usr/bin/python3
"""Module that defines a class MyList."""


class MyList(list):
    """Create a class Mylist that inherits from list."""
    def print_sorted(self):
        """Print the list, but sorted."""
        result = sorted(self)
        print(MyList(result))
