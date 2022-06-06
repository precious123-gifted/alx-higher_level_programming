#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        maxx = my_list[0]
        for i in my_list:
            if i > maxx:
                maxx = i
        return maxx
