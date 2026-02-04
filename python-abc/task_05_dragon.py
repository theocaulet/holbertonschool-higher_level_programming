#!/usr/bin/python3
"""Create a mixin class for swimming behavior."""


class SwimMixin:
    """Create a mixin class for swimming behavior."""
    def swim(self):
        """Define swim method."""
        print("The creature swims!")


class FlyMixin:
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
