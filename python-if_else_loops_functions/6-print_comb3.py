#!/usr/bin/python3
for first_digit in range(0, 10):
    for second_digit in range(0, 10):
        if first_digit == 8 and second_digit == 9:
            print("{:d}{:d}".format(first_digit, second_digit))
        if first_digit < second_digit:
            print("{:d}{:d}".format(first_digit, second_digit), end=', ')
