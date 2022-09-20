#!/usr/bin/python3
for c in range(97, 97 + 26):
    if c not in {ord('e'), ord('q')}:
        print(f"{chr(c)}", end='')
