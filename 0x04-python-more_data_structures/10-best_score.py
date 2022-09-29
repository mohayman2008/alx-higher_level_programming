#!/usr/bin/python3
def best_score(a_dictionary):
    if type(a_dictionary) is not dict:
        return None

    max = None
    key_max = None
    for k, v in a_dictionary.items():
        if max is None or v > max:
            max = v
            key_max = k
    return key_max
