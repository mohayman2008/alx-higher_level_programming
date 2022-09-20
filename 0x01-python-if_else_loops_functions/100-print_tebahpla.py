#!/usr/bin/python3
for c in range(26, 0, -2):
    print("{}{}".format(chr(c + 96), chr(c + 63)), end='')
