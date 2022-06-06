#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    div2 = []
    for i in my_list:
        if i % 2 == 0:
            div2.append(True)
        else:
            div2.append(False)
    return div2
