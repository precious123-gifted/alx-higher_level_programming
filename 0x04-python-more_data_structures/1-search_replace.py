#!/usr/bin/python3


def search_replace(my_list, search, replace):
    newl = []
    for i in my_list:
        if i == search:
            newl += [replace]
        else:
            newl += [i]
    return newl
