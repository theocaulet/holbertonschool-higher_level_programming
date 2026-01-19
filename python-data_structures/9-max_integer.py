#!/usr/bin/python3
def max_integer(my_list=[]):
    max_value = my_list[0]
    for M in my_list:
        if M > max_value:
            max_value = M
    if my_list == []:
        return None
    else:
        return (max_value)
