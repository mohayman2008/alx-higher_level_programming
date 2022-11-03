#!/usr/bin/python3
"""This module contains the unittests of the Base class"""
import unittest
import os


try:
    import models
    from models import Base, Rectangle, Square
    from models.base import Base
except BaseException as e:
    unittest.TestCase.fail(f"Exception [{e}] raised unexpectedly!")

try:
    Counts = __import__("test_models.__init__", fromlist=[None]).Counts
except Exception:
    try:
        Counts = __import__("__init__").Counts
    except Exception:
        Counts = __import__("tests.test_models.__init__",
                            fromlist=[None]).Counts


class TestBase(unittest.TestCase, Base):
    """Tests for class Base"""

    def test_Base_id(self):
        """Initialization tests"""
        B, last = (Base, Counts.base_count)
        bases = (B(), B(), B(34983458763543), B(), B(3), B(4), B())
        ids = (last + 1, last + 2, 34983458763543, last + 3, 3, 4, last + 4)

        i = 0
        for base in bases:
            self.assertEqual(base.id, ids[i])
            del base
            i += 1
        b5 = Base()
        self.assertEqual(b5.id, last + 5)
        Counts.base_count += 5
        pass

    def test_to_json_string(self):
        """Tests for to_json_string() method"""
        func = Base.to_json_string
        for i in (None, "", [], [[]], [{}, "", {}]):
            self.assertEqual(func(i), "[]")

        self.assertEqual(func([{}]), "[{}]")
        self.assertEqual(func([{'width': 1}]), '[{"width": 1}]')
        self.assertEqual(func([{'width': 1, "hello": "xs"}]),
                         '[{"width": 1, "hello": "xs"}]')
        self.assertEqual(func([{'width': 1, "hello": "xs"}, {}]),
                         '[{"width": 1, "hello": "xs"}, {}]')
        self.assertEqual(func([{'width': 1, "hello": "xs"}, {'x': 2}]),
                         '[{"width": 1, "hello": "xs"}, {"x": 2}]')
        pass

    def test_from_json_string(self):
        """Tests for from_json_string() method"""
        func = Base.from_json_string
        for i in (None, "", []):
            self.assertEqual(func(i), [])

        self.assertEqual(func("[{}]"), [{}])
        self.assertEqual(func('[{"width": 1}]'), [{'width': 1}])
        self.assertEqual(func('[{"width": 1, "hello": "xs"}, {}]'),
                         [{'width': 1, 'hello': 'xs'}, {}])
        pass

    def test_save_load(self):
        """Tests for save_to_file() and load_from_file() class method"""
        # Rectangle save-load tests
        Counts.init_rect_count()
        last = Counts.rect_count

        R, S = Rectangle, Square
        save, load = Rectangle.save_to_file, Rectangle.load_from_file
        fn = "Rectangle.json"
        if os.path.exists(fn):
            os.remove(fn)
        self.assertEqual(load(), [])

        for inp in (None, []):
            save(inp)
            self.assertEqual(load(), [])

        inputs = ([R(2, 4)], [R(2, 4), R(4, 2, 1, 2, 300)])
        Counts.rect_count += 2
        # Rectangle represented as (id, width, height, x, y)
        results = ([(last + 1, 2, 4, 0, 0)],
                   [(last + 2, 2, 4, 0, 0), (300, 4, 2, 1, 2)])

        i = 0
        for inp in inputs:
            save(inp)
            rects = load()
            Counts.rect_count += len(rects)
            j = 0
            for rect in rects:
                self.assertEqual(rect.id, results[i][j][0])
                self.assertEqual(rect.width, results[i][j][1])
                self.assertEqual(rect.height, results[i][j][2])
                self.assertEqual(rect.x, results[i][j][3])
                self.assertEqual(rect.y, results[i][j][4])
                j += 1
            i += 1
            pass

        # Square save-load tests
        Counts.init_square_count()
        last = Counts.square_count

        save, load = Square.save_to_file, Square.load_from_file
        fn = "Square.json"
        if os.path.exists(fn):
            os.remove(fn)
        self.assertEqual(load(), [])

        for inp in (None, []):
            save(inp)
            self.assertEqual(load(), [])

        inputs = ([S(2)], [S(2), S(4, 1, 2, 300)])
        Counts.square_count += 2
        # Square represented as (id, size, x, y)
        results = ([(last + 1, 2, 0, 0)],
                   [(last + 2, 2, 0, 0), (300, 4, 1, 2)])

        i = 0
        for inp in inputs:
            save(inp)
            objs = load()
            Counts.square_count += len(objs)
            j = 0
            for obj in objs:
                self.assertEqual(obj.id, results[i][j][0])
                self.assertEqual(obj.size, results[i][j][1])
                self.assertEqual(obj.x, results[i][j][2])
                self.assertEqual(obj.y, results[i][j][3])
                j += 1
            i += 1
            pass
    pass
