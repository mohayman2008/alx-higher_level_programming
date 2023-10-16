#!/usr/bin/python3
'''This script takes GitHub credentials (username and password) and uses the \
GitHub API to display the associated id'''
from sys import argv

import requests
HTTPBasicAuth = requests.auth.HTTPBasicAuth


def main():
    '''Main function'''
    if len(argv) < 3:
        print("None")
        return

    auth = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get('https://api.github.com/user', auth=auth)
    try:
        id = response.json().get('id', None)
        print(id)
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
