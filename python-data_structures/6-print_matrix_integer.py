#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for int in matrix:
        for num in int:
            if num != int[-1]:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num), end="")
        print()
