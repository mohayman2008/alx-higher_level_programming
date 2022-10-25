#!/usr/bin/python3
"""This module adds all arguments to a Python list, extends the list stored
as in json file 'add_item.json' and then writes the list back"""
import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    old_list = []
    filename = "add_item.json"
    try:
        old_list = load_from_json_file(filename)
    except Exception:
        pass
    new_list = old_list + argv[1:]
    save_to_json_file(new_list, filename)


if __name__ == "__main__":
    main()
