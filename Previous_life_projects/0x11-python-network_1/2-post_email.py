#!/usr/bin/python3
'''This script takes URL and an email as arguments, sends a POST request \
to the URL with the email as a parameter and displays the body of the \
response (decoded in utf-8)'''
from sys import argv

from urllib.parse import urlencode
from urllib.request import urlopen, Request
# urlopen = request.urlopen


def main():
    '''Main function'''
    if len(argv) < 3:
        return None

    data = urlencode({'email': str(argv[2])}).encode('ascii')
    req = Request(str(argv[1]), data, method='post')
    with urlopen(req) as res:
        print(res.read().decode('utf-8'))


if __name__ == "__main__":
    main()
