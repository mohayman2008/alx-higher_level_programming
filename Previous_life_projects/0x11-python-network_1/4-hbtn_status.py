#!/usr/bin/python3
'''This script fetches the URL "https://alx-intranet.hbtn.io/status"'''
import requests

if __name__ == "__main__":
    res = requests.get('https://alx-intranet.hbtn.io/status')
    result = res.text
    print("Body response:")
    print(f'\t- type: {type(result)}')
    print(f'\t- content: {result}')
