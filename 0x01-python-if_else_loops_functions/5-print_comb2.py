#!/usr/bin/python3
for n in range(100):
    if (n == 99):
        print("{0:02d}".format(n))
    else:
        print("{0:02d}".format(n), end=', ')
