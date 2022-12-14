#!/usr/bin/python3
"""This module contains the unittests of the Base class"""
import unittest
from io import StringIO
import sys
import os


try:
    from models import Base, Rectangle
except BaseException as e:
    print("||FAILURE||")
    unittest.TestCase.fail(f"Exception [{e}] raised unexpectedly!")

try:
    Counts = __import__("test_models.__init__", fromlist=[None]).Counts
except Exception:
    try:
        Counts = __import__("__init__").Counts
    except Exception:
        Counts = __import__("tests.test_models.__init__",
                            fromlist=[None]).Counts


class TestRectangle(unittest.TestCase):
    """Tests for class Base"""

    def test_validation(self):
        """Unit tests for validation methods"""
        vi = Rectangle.validate_int
        vgt0 = Rectangle.validate_gt0
        vge0 = Rectangle.validate_ge0

        # Rectangle.validate_int tests
        self.assertRaisesRegex(TypeError, "name must be an integer",
                               vi, "name", "21")
        self.assertRaisesRegex(TypeError, "name must be an integer",
                               vi, "name", [])
        self.assertRaisesRegex(TypeError, "xxx must be an integer",
                               vi, "xxx", 21.5)
        self.assertRaisesRegex(TypeError, " must be an integer", vi, "", None)
        self.assertRaisesRegex(TypeError, "None must be an integer",
                               vi, None, "21")

        # Rectangle.validate_gt0 tests
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               vgt0, "height", -5)
        self.assertRaisesRegex(ValueError, " must be > 0",
                               vgt0, "", 0)

        # Rectangle.validate_ge0 tests
        self.assertRaisesRegex(ValueError, "hello must be >= 0",
                               vge0, "hello", -5)
        self.assertRaisesRegex(ValueError, "() must be >= 0",
                               vge0, (), -65468746354168746325168241)
        self.assertRaisesRegex(ValueError, "False must be >= 0",
                               vge0, False, -1)
        pass

    def test_init(self):
        """Initialization tests"""
        # self.id tests

        Counts.init_rect_count()
        R, last, last_base = (Rectangle, Counts.rect_count, Counts.base_count)
        rects = [R(10, 10), R(10, 10), R(10, 10), Base(), R(10, 10, id=20),
                 R(10, 10, id="ss"), R(10, 10, id=[]), R(10, 10), Base()]
        ids = [last + 1, last + 2, last + 3, last_base + 1, 20, 'ss', [],
               last + 4, last_base + 2]
        self.assertTrue(len(ids) == len(rects))

        i = 0
        for obj in rects:
            self.assertEqual(obj.id, ids[i])
            del obj
            i += 1
        r1 = R(1, 1)
        self.assertEqual(r1.id, last + 5)
        Counts.rect_count += 5
        Counts.base_count += 2

        # Raises
        # width
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               Rectangle, "5", 3)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, 0, 3)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               Rectangle, -2, 3)
        # height
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               Rectangle, 10, "5")
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 10, 0)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               Rectangle, 10, -2)
        # x
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               Rectangle, 10, 10, "5")
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               Rectangle, 10, 10, -2)
        # y
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               Rectangle, 10, 10, 0, "5")
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               Rectangle, 10, 10, 0, -2)
        pass

    def test_set_get(self):
        """Tests for setters and getters"""
        Counts.init_rect_count()
        R, last = (Rectangle, Counts.rect_count)
        rects = [R(4, 8), R(10, 10, 5), R(10, 10, 5, 5), R(10, 10, 5, 0),
                 R(10, 10, 0, 5), R(10, 10, 0, 0), R(10, 10, id=20),
                 R(10, 10, 3, id=205), R(10, 10, 3, 2, id=35),
                 R(10, 10, 3, 2, 11), R(10, 10, 0, 0, 30)]
        ids = [last + 1, last + 2, last + 3, last + 4, last + 5, last + 6,
               20, 205, 35, 11, 30]
        Counts.rect_count += 6
        width_vals = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        height_vals = [8, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        x_vals = [0, 5, 5, 5, 0, 0, 0, 3, 3, 3, 0]
        y_vals = [0, 0, 5, 0, 5, 0, 0, 0, 2, 2, 0]
        vals = (ids, width_vals, height_vals, x_vals, y_vals)
        self.assertTrue(all(len(x) == len(rects) for x in vals))

        i = 0
        for rect in rects:
            self.assertEqual(rect.id, ids[i])
            self.assertEqual(rect.width, width_vals[i])
            self.assertEqual(rect.height, height_vals[i])
            self.assertEqual(rect.x, x_vals[i])
            self.assertEqual(rect.y, y_vals[i])
            i += 1
        pass

    def test_update(self):
        """Tests for setters and getters"""
        # Raises
        rect = Rectangle(10, 10, id=1000)
        # width
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               rect.update, 1000, "5", 3)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               rect.update, 1000, 0, 3)
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               rect.update, 1000, -2, 3)
        # height
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               rect.update, 1000, 10, "5")
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               rect.update, 1000, 10, 0)
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               rect.update, 1000, 10, -2)
        # x
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               rect.update, 1000, 10, 10, "5")
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               rect.update, 1000, 10, 10, -2)
        # y
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               rect.update, 1000, 10, 10, 0, "5")
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               rect.update, 1000, 10, 10, 0, -2)

        rect = Rectangle(10, 10, 5, 5, id=1000)
        updates = [("hs",), (300, 8), (300, 8, 16), (300, 8, 16, 0),
                   (500, 2, 2, 6, 0), (1000, 10, 10, 5, 5)]
        kw_updates = [{"id": "hs"}, {"id": 300, "width": 8},
                      {"id": 300, "width": 8, "height": 16},
                      {"id": 300, "width": 8, "height": 16, "x": 0},
                      {"id": 500, "width": 2, "height": 2, "x": 6, "y": 0},
                      {"id": 1000, "width": 10, "height": 10, "x": 5, "y": 5}]
        ids = ["hs", 300, 300, 300, 500, 1000]
        width_vals = [10, 8, 8, 8, 2, 10]
        height_vals = [10, 10, 16, 16, 2, 10]
        x_vals = [5, 5, 5, 0, 6, 5]
        y_vals = [5, 5, 5, 5, 0, 5]
        vals = (ids, width_vals, height_vals, x_vals, y_vals)
        self.assertTrue(len(updates) == len(kw_updates))
        self.assertTrue(all(len(x) == len(updates) for x in vals))

        k = 0
        for update_args in (updates, kw_updates):
            i = 0
            for update in update_args:
                if not k:
                    rect.update(*update)
                else:
                    rect.update(**update)
                self.assertEqual(rect.id, ids[i])
                self.assertEqual(rect.width, width_vals[i])
                self.assertEqual(rect.height, height_vals[i])
                self.assertEqual(rect.x, x_vals[i])
                self.assertEqual(rect.y, y_vals[i])
                i += 1
            k += 1
            pass
        # Check that keyword args are ignored if there are positional args
        rect.update("Preferred", id="Ignored")
        self.assertEqual(rect.id, 'Preferred')

        # Check that each attribute can set individually using **kwargs
        rect.update(width=8)
        self.assertEqual(rect.width, 8)
        rect.update(height=16)
        self.assertEqual(rect.height, 16)
        rect.update(x=2)
        self.assertEqual(rect.x, 2)
        rect.update(y=3)
        self.assertEqual(rect.y, 3)
        rect.update(id=1000)
        self.assertEqual(rect.id, 1000)

        # Invalid keyword arguments handling
        self.assertRaises(ValueError, rect.update, width=0)
        self.assertRaises(TypeError, rect.update, x="aa")

        # Check that not ordered **kwargs are assigned correctly
        rect.update(x=17, height=30, width=60, id=50, y=12)
        self.assertEqual(rect.width, 60)
        self.assertEqual(rect.height, 30)
        self.assertEqual(rect.x, 17)
        self.assertEqual(rect.y, 12)
        self.assertEqual(rect.id, 50)

        # Check that invalid attributes are not assigned
        rect.update(hello="world")
        self.assertNotIn("hello", rect.__dict__)
        pass

    def test_display(self):
        """Tests for display method"""
        R = Rectangle
        rects = [R(2, 2, id=30), R(1, 5, id=30), R(5, 1, id=30),
                 R(1, 1, id=30), R(1, 1, 1, 1, id=30), R(1, 1, 1, 0, id=30),
                 R(1, 1, 0, 1, id=30), R(2, 2, 1, 1, id=30),
                 R(2, 2, 1, 0, id=30), R(2, 2, 0, 1, id=30)]
        outputs = ['##\n##\n', '#\n#\n#\n#\n#\n', '#####\n', '#\n', '\n #\n',
                   ' #\n', '\n#\n', '\n ##\n ##\n', ' ##\n ##\n', '\n##\n##\n']
        self.assertTrue(len(rects) == len(outputs))

        i = 0
        for rect in rects:
            sys.stdout = StringIO()
            rect.display()
            self.assertEqual(sys.stdout.getvalue(), outputs[i])
            i += 1

        sys.stdout = sys.__stdout__
        pass

    def test_str(self):
        """Tests for __str__ method"""
        R = Rectangle
        rects = [R(2, 2, 1, 5, 30), R(1, 5, 7, 9, 30), R(5, 1, id=[]),
                 R(1, 1, 1, id=30), R(31241546, 56433446, 5416, 645, 3150666),
                 R(1, 1, id="0")]
        outputs = ['[Rectangle] (30) 1/5 - 2/2', '[Rectangle] (30) 7/9 - 1/5',
                   '[Rectangle] ([]) 0/0 - 5/1', '[Rectangle] (30) 1/0 - 1/1',
                   '[Rectangle] (3150666) 5416/645 - 31241546/56433446',
                   '[Rectangle] (0) 0/0 - 1/1']
        self.assertTrue(len(rects) == len(outputs))

        i = 0
        for rect in rects[:3]:
            self.assertEqual(str(rect), outputs[i])
            i += 1
        pass

    def test_area(self):
        """Tests for area() method"""
        R = Rectangle
        rects = [R(2, 2, 1, 5, 30), R(1, 5, 7, 9, 30), R(5, 1, id=[]),
                 R(1, 1, 1, id=30), R(31241546, 56433446, 5416, 645, 3150666)]
        outputs = [4, 5, 5, 1, 1763068099147516]
        self.assertTrue(len(rects) == len(outputs))

        i = 0
        for rect in rects:
            self.assertEqual(rect.area(), outputs[i])
            i += 1
        pass

    def test_to_dictionary(self):
        """Tests for to_dictionary() method"""
        R = Rectangle
        rects = [R(2, 2, 1, 5, 30), R(1, 5, 7, 9, 30), R(5, 1, id=[]),
                 R(1, 1, 1, id=30), R(31241546, 56433446, 5416, 645, 3150666)]
        outputs = [{'id': 30, 'width': 2, 'height': 2, 'x': 1, 'y': 5},
                   {'id': 30, 'width': 1, 'height': 5, 'x': 7, 'y': 9},
                   {'id': [], 'width': 5, 'height': 1, 'x': 0, 'y': 0},
                   {'id': 30, 'width': 1, 'height': 1, 'x': 1, 'y': 0},
                   {'id': 3150666, 'width': 31241546, 'height': 56433446,
                    'x': 5416, 'y': 645}]
        self.assertTrue(len(rects) == len(outputs))

        i = 0
        for rect in rects[:3]:
            self.assertEqual(rect.to_dictionary(), outputs[i])
            i += 1
        pass

    def test_create(self):
        """Tests for classmethod create()"""
        # Raises
        R = Rectangle
        Counts.init_rect_count()
        dicts = ({"width": "5"}, {"width": 0}, {"width": -2}, {"height": "5"},
                 {"height": 0}, {"height": -2}, {"x": "5"}, {"x": -2},
                 {"y": "5"}, {"y": -2})

        # size
        self.assertRaisesRegex(TypeError, "width must be an integer",
                               R.create, **dicts[0])
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               R.create, **dicts[1])
        self.assertRaisesRegex(ValueError, "width must be > 0",
                               R.create, **dicts[2])
        # height
        self.assertRaisesRegex(TypeError, "height must be an integer",
                               R.create, **dicts[3])
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               R.create, **dicts[4])
        self.assertRaisesRegex(ValueError, "height must be > 0",
                               R.create, **dicts[5])
        # x
        self.assertRaisesRegex(TypeError, "x must be an integer",
                               R.create, **dicts[6])
        self.assertRaisesRegex(ValueError, "x must be >= 0",
                               R.create, **dicts[7])
        # y
        self.assertRaisesRegex(TypeError, "y must be an integer",
                               R.create, **dicts[8])
        self.assertRaisesRegex(ValueError, "y must be >= 0",
                               R.create, **dicts[9])
        Counts.rect_count += len(dicts)

        # Check cases where invalid types are passed to create
        with self.assertRaises(TypeError):
            R.create(**"")
        with self.assertRaises(TypeError):
            R.create("")
        with self.assertRaises(TypeError):
            R.create(None)

        # Default dummy values used: width = 10 and height = 10
        DW = 10
        DH = 10
        last = Counts.rect_count

        dicts = [{}, {"id": "hs"}, {"id": 300, "width": 8},
                 {"id": 300, "width": 8, "height": 16},
                 {"id": 300, "width": 8, "height": 16, "x": 0},
                 {"id": 500, "width": 2, "height": 2, "x": 6, "y": 5},
                 {"width": 8}, {"height": 40}, {"x": 2}, {"y": 3}]
        ids = [last + 1, "hs", 300, 300, 300, 500, last + 7, last + 8,
               last + 9, last + 10]
        width_vals = [DW, DW, 8, 8, 8, 2, 8, DW, DW, DW]
        height_vals = [DH, DH, DH, 16, 16, 2, DH, 40, DH, DH]
        x_vals = [0, 0, 0, 0, 0, 6, 0, 0, 2, 0]
        y_vals = [0, 0, 0, 0, 0, 5, 0, 0, 0, 3]
        vals = (ids, width_vals, height_vals, x_vals, y_vals)
        self.assertTrue(all(len(x) == len(dicts) for x in vals))

        i = 0
        for d in dicts:
            rect = R.create(**d)
            self.assertEqual(rect.id, ids[i])
            self.assertEqual(rect.width, width_vals[i])
            self.assertEqual(rect.height, height_vals[i])
            self.assertEqual(rect.x, x_vals[i])
            self.assertEqual(rect.y, y_vals[i])
            i += 1
        Counts.rect_count += len(dicts)

        # Check that not ordered **kwargs are assigned correctly
        rect = R.create(height=304, x=17, width=60, id=50, y=12)
        self.assertEqual(rect.width, 60)
        self.assertEqual(rect.x, 17)
        self.assertEqual(rect.height, 304)
        self.assertEqual(rect.y, 12)
        self.assertEqual(rect.id, 50)

        # Check that invalid attributes are not assigned
        rect = R.create(hello="world")
        self.assertNotIn("hello", rect.__dict__)

        Counts.rect_count += 2
        pass

    def test_save_load(self):
        """Tests for save_to_file() and load_from_file() class method"""
        # Rectangle save-load tests
        Counts.init_rect_count()
        last = Counts.rect_count

        R = Rectangle
        save, load = Rectangle.save_to_file, Rectangle.load_from_file
        fn = "Rectangle.json"
        if os.path.exists(fn):
            os.remove(fn)
        self.assertEqual(load(), [])

        for inp in (None, []):
            save(inp)
            self.assertEqual(load(), [])
            os.remove(fn)

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
            self.assertNotEqual(len(rects), 0)
            for rect in rects:
                self.assertEqual(rect.id, results[i][j][0])
                self.assertEqual(rect.width, results[i][j][1])
                self.assertEqual(rect.height, results[i][j][2])
                self.assertEqual(rect.x, results[i][j][3])
                self.assertEqual(rect.y, results[i][j][4])
                j += 1
            i += 1
            os.remove(fn)
            pass
    pass
