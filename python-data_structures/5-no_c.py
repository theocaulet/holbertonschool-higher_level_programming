#!/usr/bin/python3
def no_c(my_string):
    for str in my_string:
        if str == 'c' or str == 'C':
            continue
        print("{}".format(str), end='')
    return str
