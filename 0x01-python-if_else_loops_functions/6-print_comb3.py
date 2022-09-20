#!/usr/bin/python3
for n1 in range(10):
    for n2 in range(n1 + 1, 10):
        if (n1 == 0 and n2 == 1):
            print(f"{n1:d}{n2:d}", end='')
        else:
            print(f", {n1:d}{n2:d}", end='')
print()
