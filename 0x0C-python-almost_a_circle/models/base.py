#!/usr/bin/python3
"""This module contains the definition of the Base class"""
import json
import csv
try:
    import turtle
except ModuleNotFoundError:
    pass


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
        if type(dictionary) is not dict:  # or not len(dictionary):
            return None
        if cls.__name__ not in ("Square", "Rectangle"):
            return None
        if cls.__name__ == "Square":
            obj = cls(10)
        elif cls.__name__ == "Rectangle":
            obj = cls(10, 10)
        obj.update(**dictionary)
        return obj

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if type(list_dictionaries) is not list or\
           any(type(x) is not dict for x in list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

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
            return [cls.create(**d) for d in list_dicts]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return list()
        pass

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the csv representation of a list of objects of class cls
        to a file"""
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Square":
            fields = ("id", "size", "x", "y")
        elif cls.__name__ == "Rectangle":
            fields = ("id", "width", "height", "x", "y")

        if type(list_objs) is not list:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fields)
            writer.writeheader()
            writer.writerows(list_dicts)
        pass

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances of class cls by loading from
        respective csv file"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'r', encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            list_dicts = [{k: int(v) for k, v in d.items()} for d in reader]
        return [cls.create(**d) for d in list_dicts]
        pass

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles in list_rectangles and Squares in list_squares"""
        if "turtle" not in globals().keys():
            print("turtle wasn't found!")
            return
        WIDTH, HEIGHT = 800, 600

        screen = turtle.Screen()
        screen.setup(WIDTH, HEIGHT)
        screen.screensize(WIDTH + 4, HEIGHT + 8)
        screen.setworldcoordinates(-2, HEIGHT + 4, WIDTH + 2, -4)

        rects = []
        for l_obj in (list_rectangles, list_squares):
            if type(l_obj) is list:
                rects += l_obj
        colors = ("red", "green", "blue", "black", "grey", "orange",
                  "purple")
        tu = turtle.Turtle()
        turtle.screensize(600, 450)
        tu.screen.bgcolor("white")
        tu.pensize(3)
        tu.shape("turtle")

        count = 0
        for r in rects:
            tu.up()
            tu.goto(r.x, r.y)
            tu.color(colors[count % len(colors)])
            tu.fillcolor(colors[len(colors) - 1 - count % len(colors)])
            tu.showturtle()
            tu.down()
            for i in range(2):
                tu.forward(r.width)
                tu.right(90)
                tu.forward(r.height)
                tu.right(90)
            tu.hideturtle()
            count += 1

        # turtle.done()
        turtle.exitonclick()
        pass
    pass
