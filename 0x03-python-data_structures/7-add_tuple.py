#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= 2:
        copyta = tuple_a[:2]
    else:
        if len(tuple_a) == 1:
            copyta = tuple_a[0], 0
        else:
            copyta = 0, 0
    if len(tuple_b) >= 2:
        copytb = tuple_b[:2]
    else:
        if len(tuple_b) == 1:
            copytb = tuple_b[0], 0
        else:
            copytb = 0, 0
    return (copyta[0] + copytb[0], copyta[1] + copytb[1])
