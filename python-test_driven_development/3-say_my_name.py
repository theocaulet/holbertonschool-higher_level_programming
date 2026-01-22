#!/usr/bin/python3
"""Function that print a person's name."""


def say_my_name(first_name, last_name=""):
    """
    Print a person's full name.

    Args:
    first_name: first name of the person
    last_name: last name of the person

    Raises:
    TypeError: if first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {} ".format(first_name))
