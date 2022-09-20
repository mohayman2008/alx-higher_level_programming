#!/usr/bin/python3
for n1 in range(10):
    for n2 in range(n1 + 1, 10):
        if (n1 == 0 and n2 == 1):
            print("{0:d}{1:d}".format(n1, n2), end='')
        else:
            print(", {0:d}{1:d}".format(n1, n2), end='')
print()
