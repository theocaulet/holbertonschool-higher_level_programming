#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for char in str:
        if 97 <= char <= 122:
            upper += chr(ord(char) - 32)
        else:
            upper += char
    print("{}".format(upper))
