#!/usr/bin/python3
"""This module contains the definition of the Base class"""
import json


class Base:
    """Definition of the Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Objects of class Base constructor"""
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
        pass

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of class cls with attributes set
        according to dictionary"""
        obj = cls(10, 10, id=80000)
        obj.update(**dictionary)
        return obj

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries"""
        # if (type(list_dictionaries) is not list)
        # or not len(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        try:
            return json.dumps(list_dictionaries)
        except TypeError:
            return json.dumps([])

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of dictionaries represented by a JSON string"""
        if (type(json_string) is not str) or not len(json_string):
            return list()
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a list of objects
        of class Base or of a class that inherits from Base to a file"""
        filename = "{}.json".format(cls.__name__)
        with open(filename, 'w', encoding='utf-8') as f:
            if type(list_objs) is not list:
                list_dicts = []
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
            f.write(cls.to_json_string(list_dicts))
        pass

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances of class cls by loading from
        respective json file"""
        filename = "{}.json".format(cls.__name__)
        list_objs = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                list_dicts = cls.from_json_string(f.read())
                for dictionary in list_dicts:
                    list_objs.append(cls.create(**dictionary))
                return list_objs
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return list()
        pass
    pass
