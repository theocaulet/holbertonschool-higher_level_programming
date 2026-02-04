#!/usr/bin/python3
"""Module that creates a CountedIterator class.

CountedIterator is a custom iterator that wraps any iterable and counts
how many items have been iterated through.
"""


class CountedIterator:
    """An iterator wrapper that counts the number of iterations.

    Attributes:
        iterable: The wrapped iterator object.
        count: The number of items iterated through.
    """

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable.

        Args:
            iterable: Any iterable object (list, tuple, string, etc.).
        """
        self.__iterable = iter(iterable)
        self.__count = 0

    def get_count(self):
        """Get the current count of iterations.

        Returns:
            int: The number of items iterated through so far.
        """
        return self.__count

    def __next__(self):
        """Return the next item from the iterable and increment count.

        Returns:
            The next item from the wrapped iterable.

        Raises:
            StopIteration: When the iterable is exhausted.
        """
        try:
            item = next(self.__iterable)
            self.__count += 1
            return item
        except StopIteration:
            raise StopIteration
