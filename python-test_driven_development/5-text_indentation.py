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
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    # Loop through the text
    while i < length:
        # If the character is a separator, print it and add 2 new lines
        if text[i] in ['.', '?', ':']:
            print(text[i])
            print()  # Print 2 new lines
            i += 1
            # Skip spaces after the separator
            while i < length and text[i] == ' ':
                i += 1
        else:
            # Print the character
            print(text[i], end='')
            i += 1
