#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = ord(c)
        if char >= 97 and char < 97 + 26:
            c = chr(char - 32)
        print("{}".format(c), end='')
    print()
