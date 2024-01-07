#!/usr/bin/python3
'''This script takes URL and an email as arguments, sends a POST request \
to the URL with the email as a parameter and displays the body of the response
'''
from sys import argv

import requests


def main():
    '''Main function'''
    if len(argv) < 3:
        return None

    response = requests.post(str(argv[1]), data=[('email', argv[2])])
    print(response.text)


if __name__ == "__main__":
    main()
