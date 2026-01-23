#!/usr/bin/python3
"""Unitest for max_integer([..]) function."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_positive_integers(self):
        """Test with positive integers."""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_negative_integers(self):
        """Test with negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1)

    def test_mixed_integers(self):
        """Test with mixed positive and negative integers."""
        self.assertEqual(max_integer([-10, 0, 10, 5, -5]), 10)

    def test_single_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        """Test with float numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5, -1.5]), 2.5)

    def test_mixed_numbers(self):
        """Test with mixed integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3, -4.5, 0]), 3)

    def test_strings(self):
        """Test with a list of strings."""
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_mixed_types(self):
        """Test with mixed types should raise TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])
