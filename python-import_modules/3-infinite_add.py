#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    nums = list(map(int, argv[1:]))
    print("{}".format(sum(nums)))
