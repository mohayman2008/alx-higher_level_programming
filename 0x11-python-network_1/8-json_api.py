#!/usr/bin/python3
'''This script takes a letter as an argument, sends a POST request to \
"http://0.0.0.0:5000/search_user" with the letter as a parameter and \
displays the returned data'''
from sys import argv

import requests
# JSONDecodeError = requests.exceptions.JSONDecodeError


def main():
    '''Main function'''
    data = {'q': ''}
    if len(argv) >= 2:
        data['q'] = argv[1]
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        result = response.json()
        id = result.get('id', None)
        name = result.get('name', None)
        if id is None or name is None:
            print('No result')
        else:
            print(f'[{id}] {name}')
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
