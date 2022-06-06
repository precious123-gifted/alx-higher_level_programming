#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    copylist = my_list[:]
    if idx >= 0 and idx <= len(copylist) - 1:
        copylist[idx] = element
    return copylist
