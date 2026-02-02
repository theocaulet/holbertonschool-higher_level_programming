#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        result = sorted(self)
        print(MyList(result))
