#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        best_k = max(a_dictionary.values())
        return [i for i, num in a_dictionary.items() if num == best_k][0]
