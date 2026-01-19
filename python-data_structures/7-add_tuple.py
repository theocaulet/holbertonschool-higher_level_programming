#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = [0, 0]
    b = [0, 0]
    if len(tuple_a) > 0:
        a[0] = tuple_a[0]
    else:
        a[0] = 0
    if len(tuple_a) > 1:
        a[1] = tuple_a[1]
    else:
        a[1] = 0
    if len(tuple_b) > 0:
        b[0] = tuple_b[0]
    else:
        b[0] = 0
    if len(tuple_b) > 1:
        b[1] = tuple_b[1]
    else:
        b[1] = 0
    return (a[0] + b[0], a[1] + b[1])
