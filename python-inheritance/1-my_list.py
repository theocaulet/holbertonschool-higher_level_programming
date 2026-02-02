#!/usr/bin/python3
class MyList(list):
    """Create a class Mylist that inherits from list."""
    def print_sorted(self):
        """Print the list, but sorted."""
        result = sorted(self)
        print(MyList(result))
