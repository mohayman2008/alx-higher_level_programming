#!/usr/bin/python3
'''This script sends a request to a URL as an argument  and displays the body\
 of the response'''

from sys import argv

import requests


def main():
    '''Main function'''
    if len(argv) < 2:
        return None

    response = requests.get(str(argv[1]))
    if response.status_code == 200:
        print(response.text)
    else:
        print(f'Error code: {response.status_code}')


if __name__ == "__main__":
    main()
