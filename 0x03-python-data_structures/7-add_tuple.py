#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2]
    b = tuple_b[:2]
    if len(a) < 2:
        a += (0,) * (2 - len(a))
    if len(b) < 2:
        b += (0,) * (2 - len(b))
    new_tuple = (a[0] + b[0], a[1] + b[1])
    return new_tuple
