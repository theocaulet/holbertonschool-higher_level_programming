#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    t = tuple_a + tuple_b
    if len(t) < 2:
        t += (0, 0, 0, 0)
    elif len(t) > 2:
        t = t[:4]
    t += (0, 0, 0, 0)
    return (t[0] + t[2], t[1] + t[3])
