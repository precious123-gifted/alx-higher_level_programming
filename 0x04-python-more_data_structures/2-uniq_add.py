#!/usr/bin/python3


def uniq_add(my_list=[]):
    r = 0
    uni = set(my_list)
    for i in uni:
        r += i
    return r
