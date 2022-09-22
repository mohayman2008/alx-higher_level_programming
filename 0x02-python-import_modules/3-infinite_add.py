#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    sum = 0
    for arg in argv[1:]:
        sum += int(arg)

    print(f"{sum:d}")
