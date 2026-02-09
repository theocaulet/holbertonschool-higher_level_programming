#!/usr/bin/python3
import sys
"""Script that adds all arguments to a Python list."""
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
if __name__ == "__main__":
    """Add all arguments to a Python list, and then save them to a file."""
    filename = "add_item.json"
    my_list = load_from_json_file(filename)
    if my_list is None:
        my_list = []
    arguments = sys.argv[1:]
    my_list.extend(arguments)
    save_to_json_file(my_list, filename)
