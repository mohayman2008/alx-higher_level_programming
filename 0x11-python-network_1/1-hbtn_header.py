#!/usr/bin/python3
'''This script takes in a URL as argument, sends a request to the URL \
and displays the value of the "X-Request-Id" header of the response.'''
from sys import argv

from urllib import request
urlopen = request.urlopen


def main():
    '''Main function'''
    if len(argv) < 2:
        return None

    with urlopen(str(argv[1])) as res:
        val = res.info().get('X-Request-Id', None)
    if val is not None:
        print(val)


if __name__ == "__main__":
    main()
