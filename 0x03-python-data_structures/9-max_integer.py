#!/usr/bin/python3
def max_integer(my_list=[]):
    n_max = None
    for num in my_list:
        if n_max is None or num > n_max:
            n_max = num
    return n_max
