#!/usr/bin/python3
"""Function that prints a text with 2 new lines"""


def text_indentation(text):
    """
    Print a text with 2 new_lines

    Args:
    text: text to be printed
    Raises:
    TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    length = len(text)
    while i < length and text[i] == ' ':
        i += 1
    while i < length:
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print("\n")
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
