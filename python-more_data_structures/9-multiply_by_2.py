#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for num in new_dictionary:
        if new_dictionary[num] * 2 == 0:
            new_dictionary[num] = True
        else:
            new_dictionary[num] *= 2
    return new_dictionary
