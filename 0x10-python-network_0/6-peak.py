#!/usr/bin/python3
'''This module contains the definition of "find_peak" function'''


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers'''
    if not isinstance(list_of_integers, list) or not list_of_integers:
        return None
    lst = list_of_integers
    length = (len(lst))
    if length == 1:
        return lst[0]
    if length == 2:
        if lst[0] >= lst[1]:
            return lst[0]
        return lst[1]

    center = int(length / 2)
    if lst[center - 1] < lst[center] > lst[center + 1]:
        return lst[center]
    if lst[center - 1] >= lst[center]:
        return find_peak(lst[:center])
    return find_peak(lst[center+1:])
