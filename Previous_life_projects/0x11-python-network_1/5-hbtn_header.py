#!/usr/bin/python3
'''This script takes in a URL as argument, sends a request to the URL \
and displays the value of the "X-Request-Id" header of the response.'''
from sys import argv

import requests


def main():
    '''Main function'''
    if len(argv) < 2:
        return None

    res = requests.get(str(argv[1]))
    val = res.headers.get('X-Request-Id', None)
    if val is not None:
        print(val)


if __name__ == "__main__":
    main()
