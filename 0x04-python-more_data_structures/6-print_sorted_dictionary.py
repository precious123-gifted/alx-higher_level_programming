#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    or_l = sorted(a_dictionary.keys())
    for i in or_l:
        print("{:s}: {}".format(i, a_dictionary[i]))
