#!/usr/bin/python3
def no_c(my_string):
    out = ''
    slice_start = 0
    for i in range(len(my_string)):
        if my_string[i] in ('c', 'C'):
            out += my_string[slice_start: i]
            slice_start = i + 1

    out += my_string[slice_start:]
    return out
