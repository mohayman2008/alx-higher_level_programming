#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or not len(my_list):
        return 0
    _sum = 0
    weights = 0
    for v, w in my_list:
        _sum += v * w
        weights += w
    return _sum / weights
