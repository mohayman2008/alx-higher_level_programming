#!/usr/bin/python3
from sys import argv

output = ""
if __name__ == '__main__':
    argc = len(argv) - 1
    output += str(argc) + " argument"
    if argc != 1:
        output += "s"
    if argc == 0:
        output += "."
    else:
        output += ":"

    print(output)

    n = 1
    for arg in argv[1:]:
        print(f"{n}: {arg}")
        n += 1
