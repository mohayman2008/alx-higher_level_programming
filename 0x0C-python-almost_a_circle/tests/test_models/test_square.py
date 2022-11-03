#!/usr/bin/python3
"""This module contains the unittests of the Square class"""
import unittest
from io import StringIO
import sys
import os


try:
    from models import Base, Rectangle, Square
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


class TestSquare(unittest.TestCase):
    """Tests for class Square"""

    def test_init(self):
        """Initialization tests"""
        # self.id tests
        Counts.init_square_count()
        Counts.init_rect_count()
        S, R = (Square, Rectangle)
        last, last_rect, last_base = (Counts.square_count, Counts.rect_count,
                                      Counts.base_count)
        if Counts.rect_count == 0:
            Counts.rect_count = 1
            last_rect = 1
        squares = [S(10), S(10), S(10), Base(), R(1, 1), S(10, id=20),
                   S(10, id="ss"), S(10, id=[]), S(10), R(1, 1), Base()]
        ids = [last + 1, last + 2, last + 3, last_base + 1, last_rect + 1, 20,
               'ss', [], last + 4, last_rect + 2, last_base + 2]
        self.assertTrue(len(ids) == len(squares))

        i = 0
        for obj in squares:
            self.assertEqual(obj.id, ids[i])
            del obj
            i += 1
        s1 = S(1, 1)
        self.assertEqual(s1.id, last + 5)
        Counts.square_count += 5
        Counts.base_count += 2
        Counts.rect_count += 2

        # Raises
        # size
        self.assertRaisesRegex(TypeError, "width must be an integer", S, "5")
        self.assertRaisesRegex(ValueError, "width must be > 0", S, 0)
        self.assertRaisesRegex(ValueError, "width must be > 0", S, -2)
        # x
        self.assertRaisesRegex(TypeError, "x must be an integer", S, 10, "5")
        self.assertRaisesRegex(ValueError, "x must be >= 0", S, 10, -2)
        # y
        self.assertRaisesRegex(TypeError, "y must be an integer", S, 10, 0,
                               "5")
        self.assertRaisesRegex(ValueError, "y must be >= 0", S, 10, 0, -2)
        pass

    def test_set_get(self):
        """Tests for setters and getters"""
        Counts.init_square_count()
        S, last = (Square, Counts.square_count)
        squares = [S(4), S(10, 5), S(10, 5, 5), S(10, 5, 0), S(10, 0, 5),
                   S(10, 0, 0), S(10, id=20), S(10, 3, id=205),
                   S(10, 3, 2, id=35), S(10, 3, 2, 11), S(10, 0, 0, 30)]
        ids = [last + 1, last + 2, last + 3, last + 4, last + 5, last + 6,
               20, 205, 35, 11, 30]
        Counts.square_count += 6
        size_vals = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        x_vals = [0, 5, 5, 5, 0, 0, 0, 3, 3, 3, 0]
        y_vals = [0, 0, 5, 0, 5, 0, 0, 0, 2, 2, 0]
        vals = (ids, size_vals, x_vals, y_vals)
        self.assertTrue(all(len(x) == len(squares) for x in vals))

        i = 0
        for s in squares:
            self.assertEqual(s.id, ids[i])
            self.assertEqual(s.size, size_vals[i])
            self.assertEqual(s.x, x_vals[i])
            self.assertEqual(s.y, y_vals[i])
            i += 1
        pass

    def test_update(self):
        """Tests for setters and getters"""
        # Raises
        sq = Square(10, id=1000)
        # size
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               sq.update, 1000, "5")
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               sq.update, 1000, 0)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               sq.update, 1000, -2)
        # x
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               sq.update, 1000, 10, "5")
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               sq.update, 1000, 10, -2)
        # y
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               sq.update, 1000, 10, 0, "5")
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               sq.update, 1000, 10, 0, -2)

        sq = Square(10, 5, 5, id=1000)
        updates = [("hs",), (300, 8), (300, 8, 0), (500, 2, 6, 0),
                   (1000, 10, 5, 5)]
        kw_updates = [{"id": "hs"}, {"id": 300, "size": 8},
                      {"id": 300, "size": 8, "x": 0},
                      {"id": 500, "size": 2, "x": 6, "y": 0},
                      {"id": 1000, "size": 10, "x": 5, "y": 5}]
        ids = ["hs", 300, 300, 500, 1000]
        size_vals = [10, 8, 8, 2, 10]
        x_vals = [5, 5, 0, 6, 5]
        y_vals = [5, 5, 5, 0, 5]
        vals = (ids, size_vals, x_vals, y_vals)
        self.assertTrue(len(updates) == len(kw_updates))
        self.assertTrue(all(len(x) == len(updates) for x in vals))

        k = 0
        for update_args in (updates, kw_updates):
            i = 0
            for update in update_args:
                if not k:
                    sq.update(*update)
                else:
                    sq.update(**update)
                self.assertEqual(sq.id, ids[i])
                self.assertEqual(sq.size, size_vals[i])
                self.assertEqual(sq.x, x_vals[i])
                self.assertEqual(sq.y, y_vals[i])
                i += 1
            k += 1
            pass
        # Check that keyword args are ignored if there are positional args
        sq.update("Preferred", id="Ignored")
        self.assertEqual(sq.id, 'Preferred')

        # Check that each attribute can set individually using **kwargs
        sq.update(size=8)
        self.assertEqual(sq.size, 8)
        sq.update(x=2)
        self.assertEqual(sq.x, 2)
        sq.update(y=3)
        self.assertEqual(sq.y, 3)
        sq.update(id=1000)
        self.assertEqual(sq.id, 1000)

        # Invalid keyword arguments handling
        self.assertRaises(ValueError, sq.update, size=0)
        self.assertRaises(TypeError, sq.update, x="aa")

        # Check that not ordered **kwargs are assigned correctly
        sq.update(x=17, size=60, id=50, y=12)
        self.assertEqual(sq.size, 60)
        self.assertEqual(sq.x, 17)
        self.assertEqual(sq.y, 12)
        self.assertEqual(sq.id, 50)

        # Check that invalid attributes are not assigned
        sq.update(hello="world")
        self.assertNotIn("hello", sq.__dict__)
        pass

    def test_display(self):
        """Tests for display method"""
        S = Square
        squares = [S(2, id=30), S(5, id=30), S(1, id=30), S(1, 1, id=30),
                   S(2, 1, 1, id=30), S(2, 0, 1, id=30)]
        outputs = ['##\n##\n', '#####\n#####\n#####\n#####\n#####\n', '#\n',
                   ' #\n', '\n ##\n ##\n', '\n##\n##\n']
        self.assertTrue(len(squares) == len(outputs))

        i = 0
        for s in squares:
            sys.stdout = StringIO()
            s.display()
            self.assertEqual(sys.stdout.getvalue(), outputs[i])
            i += 1
        sys.stdout = sys.__stdout__
        pass

    def test_str(self):
        """Tests for __str__ method"""
        S = Square
        squares = [S(2, 1, 5, 30), S(1, 7, 9, 30), S(5, id=[]), S(1, 1, id=30),
                   S(31241546, 5416, 645, 3150666), S(1, id="0")]
        outputs = ['[Square] (30) 1/5 - 2', '[Square] (30) 7/9 - 1',
                   '[Square] ([]) 0/0 - 5', '[Square] (30) 1/0 - 1',
                   '[Square] (3150666) 5416/645 - 31241546',
                   '[Square] (0) 0/0 - 1']
        self.assertTrue(len(squares) == len(outputs))

        i = 0
        for sq in squares:
            self.assertEqual(str(sq), outputs[i])
            i += 1
        pass

    def test_area(self):
        """Tests for area() method"""
        S = Square
        squares = [S(2, 1, 5, 30), S(1, 7, 9, 30), S(5, id=[]),
                   S(31241546, 5416, 645, 3150666)]
        outputs = [4, 1, 25, 31241546 ** 2]
        self.assertTrue(len(squares) == len(outputs))

        i = 0
        for sq in squares:
            self.assertEqual(sq.area(), outputs[i])
            i += 1
        pass

    def test_to_dictionary(self):
        """Tests for to_dictionary() method"""
        S = Square
        squares = [S(2, 1, 5, 30), S(1, 7, 9, 30), S(5, id=[]), S(1, 1, id=30),
                   S(31241546, 5416, 645, 3150666)]
        outputs = [{'id': 30, 'size': 2, 'x': 1, 'y': 5},
                   {'id': 30, 'size': 1, 'x': 7, 'y': 9},
                   {'id': [], 'size': 5, 'x': 0, 'y': 0},
                   {'id': 30, 'size': 1, 'x': 1, 'y': 0},
                   {'id': 3150666, 'size': 31241546, 'x': 5416, 'y': 645}]
        self.assertTrue(len(squares) == len(outputs))

        i = 0
        for sq in squares:
            self.assertEqual(sq.to_dictionary(), outputs[i])
            i += 1
        pass

    def test_create(self):
        """Tests for classmethod create()"""
        # Raises
        S = Square
        Counts.init_square_count()
        dicts = ({"size": "5"}, {"size": 0}, {"size": -2}, {"x": "5"},
                 {"x": -2}, {"y": "5"}, {"y": -2})
        # size
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               S.create, **dicts[0])
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               S.create, **dicts[1])
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               S.create, **dicts[2])
        # x
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               S.create, **dicts[3])
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               S.create, **dicts[4])
        # y
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               S.create, **dicts[5])
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               S.create, **dicts[6])
        Counts.square_count += len(dicts)

        # Check cases where invalid types are passed to create
        with self.assertRaises(TypeError):
            S.create(**"")
        with self.assertRaises(TypeError):
            S.create("")
        with self.assertRaises(TypeError):
            S.create(None)

        # Default dummy values used: size = 10
        DS = 10
        last = Counts.square_count
        dicts = [{}, {"id": "hs"}, {"id": 300, "size": 8},
                 {"id": 300, "size": 8, "x": 0},
                 {"id": 500, "size": 2, "x": 6, "y": 5},
                 {"size": 8}, {"x": 2}, {"y": 3}]
        ids = [last + 1, "hs", 300, 300, 500, last + 6, last + 7, last + 8]
        size_vals = [DS, DS, 8, 8, 2, 8, DS, DS]
        x_vals = [0, 0, 0, 0, 6, 0, 2, 0]
        y_vals = [0, 0, 0, 0, 5, 0, 0, 3]
        vals = (ids, size_vals, x_vals, y_vals)
        self.assertTrue(all(len(x) == len(dicts) for x in vals))

        i = 0
        for d in dicts:
            sq = S.create(**d)
            self.assertEqual(sq.id, ids[i])
            self.assertEqual(sq.size, size_vals[i])
            self.assertEqual(sq.x, x_vals[i])
            self.assertEqual(sq.y, y_vals[i])
            i += 1
        Counts.square_count += len(dicts)

        # Check that not ordered **kwargs are assigned correctly
        sq = S.create(x=17, size=60, id=50, y=12)
        self.assertEqual(sq.size, 60)
        self.assertEqual(sq.x, 17)
        self.assertEqual(sq.y, 12)
        self.assertEqual(sq.id, 50)

        # Check that invalid attributes are not assigned
        sq = S.create(hello="world")
        self.assertNotIn("hello", sq.__dict__)

        Counts.square_count += 2
        pass

    def test_save_load(self):
        """Tests for save_to_file() and load_from_file() class method"""
        S = Square
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
