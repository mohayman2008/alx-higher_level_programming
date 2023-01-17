#!/usr/bin/python3
'''This script fetches the URL "https://alx-intranet.hbtn.io/status"'''
from urllib import request
urlopen = request.urlopen

if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as res:
        result = res.read()
    print("Body response:")
    print(f'\t- type: {type(result)}')
    print(f'\t- content: {result}')
    print(f'\t- utf8 content: {result.decode("utf-8")}')
