#!/usr/bin/python3
"""Serialize and deserialize custom Python objects using the pickle module."""
import pickle


class CustomObject:
    """Represents a custom object
      with attributes and methods for serialization."""
    def __init__(self, name, age, is_student):
        """Initialize the CustomObject
          with name, age and is_student attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Define a method to display the attributes of the CustomObject."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Define a method to serialize
          the CustomObject instance to a file using pickle."""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Define a class method to deserialize
          a CustomObject instance from a file using pickle."""
        with open(filename, 'rb') as file:
            return pickle.load(file)
