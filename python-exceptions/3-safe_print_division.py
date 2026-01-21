#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a / b
    except ZeroDivisionError:
        return None
    else:
        return a / b
    finally:
        print("Inside result: {}".format(a, b))
