#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    v = []
    if value in a_dictionary.values():
        for i in a_dictionary:
            if a_dictionary[i] == value:
                v += [i]
        for j in v:
            del a_dictionary[j]
    return a_dictionary
