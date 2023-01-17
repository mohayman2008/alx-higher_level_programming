#!/usr/bin/python3
'''This module contains the definition of "find_peak" function'''


def find_peak(list_of_integers):
    '''Finds a peak in a list of unsorted integers'''
    if list_of_integers == []:
        return None

    lst = list_of_integers
    length = (len(lst))
    if length == 1:
        return lst[0]
    if lst[0] >= lst[1]:
        return lst[0]
    if lst[-1] >= lst[-2]:
        return lst[-1]

    for i in range(1, length - 1):
        if (lst[i - 1] <= lst[i] >= lst[i+1]):
            return lst[i]
