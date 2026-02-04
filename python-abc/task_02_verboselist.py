#!/usr/bin/python3
"""Module that creates a VerboseList class inheriting from list."""


class VerboseList(list):
    """Create a VerboseList class."""
    def append(self, item):
        """Define the append method."""
        print(f"Added {item} to the list")
        super().append(item)

    def extend(self, x):
        """Define the extend method."""
        print(f"Extended the list with {len(x)} items")
        super().extend(x)

    def remove(self, item):
        """Define the remove method."""
        print(f"Removed {item} from the list")
        super().remove(item)

    def pop(self, item=-1):
        """Define the pop method."""
        print(f"Popped {item} from the list")
        super().pop(item)
