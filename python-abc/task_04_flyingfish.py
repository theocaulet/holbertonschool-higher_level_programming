#!/usr/bin/python3
class Fish:
    """Create a Fish class."""
    def swim(self):
        """Define a method for swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Define a method for habitat."""
        print("The fish lives in water")


class Bird:
    """Create a Bird class."""
    def fly(self):
        """Define a method for flying."""
        print("The bird is flying")

    def habitat(self):
        """Define a methof for habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Create a FlyingFish class that inherits from Fish and Bird."""
    def fly(self):
        """Define a method for flying."""
        print("The flying fish is soaring!")

    def swim(self):
        """Define a method for swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Define a method for habitat."""
        print("The flying fish lives both in water and the sky!")
