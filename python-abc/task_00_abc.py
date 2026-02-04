#!/usr/bin/python3
"""Mosule that defines an abstract Animal class
 and its subclasses Dog and Cat."""
from abc import ABC, abstractmethod
"""Import the necessary components from the abc module."""


class Animal(ABC):
    """Create an Animal class."""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Create a Dog class."""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Create a Cat class."""
    def sound(self):
        return "Meow"
