#!/usr/bin/python3
def inherits_from(obj, a_class):
    """Function that returns True if the object is an instance,
      otherwise False."""
    if type(obj) is not a_class and isinstance(obj, a_class):
        return True
    else:
        return False
