#!/usr/bin/python3
"""Module that creates a CountedIterator class."""


class CountedIterator:
    """Create a class named CountedIterator."""
    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""
        self.iterable = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Define the iterator method."""
        return self

    def get_count(self):
        """Define a method to get the count of iterations."""
        return self.count

    def __next__(self):
        """Define the next method to return the next item."""
        self.count += 1
        return next(self.iterable)
