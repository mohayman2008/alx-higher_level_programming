#!/usr/bin/python3
'''This script takes in a URL as argument, sends a request to the URL \
and displays the body of the response (decoded in utf-8)'''
from sys import argv

from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError


def main():
    '''Main function'''
    if len(argv) < 2:
        return None

    try:
        with urlopen(str(argv[1])) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as err:
        print(f'Error code: {err.code}')


if __name__ == "__main__":
    main()
