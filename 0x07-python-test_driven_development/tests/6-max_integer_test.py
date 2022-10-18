#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """UnitTest class for max_integer"""

    def test_results(self):
        """Test results when no errors are expected"""
        l0 = [-5, 0, 55, 10, 55.5]
        self.assertEqual(max_integer(l0), 55.5)
        t0 = (-5, 0, 55, 10, 55.5)
        self.assertEqual(max_integer(t0), 55.5)
        l1 = [-35, -2545, -56, -5]
        self.assertEqual(max_integer(l1), -5)
        t1 = (-35, -2545, -56, -5)
        self.assertEqual(max_integer(t1), -5)
        l2 = []
        self.assertEqual(max_integer(l2), None)
        t2 = ()
        self.assertEqual(max_integer(t2), None)
        l3 = [60]
        self.assertEqual(max_integer(l3), 60)
        t3 = (60,)
        self.assertEqual(max_integer(t3), 60)
        l4 = [0, 0, 0]
        self.assertEqual(max_integer(l4), 0)
        t4 = (0,)
        self.assertEqual(max_integer(t4), 0)
        l5 = [100, 3, 50]
        self.assertEqual(max_integer(l5), 100)
        t5 = (600, 600, 500, 600)
        self.assertEqual(max_integer(t5), 600)
        l6 = [100, 3, 50, 7000, 800000000000000000000000000, 6546, -254, 0,
              1236536513545435436543654365365434, 0.000001, 0.46, 516]
        self.assertEqual(max_integer(l6), 1236536513545435436543654365365434)
        t6 = [0.1, 0.3, 0.5, 0.7, 0.800000000000000000000000001, 0.6546,
              -0.254, 0.1236536513545435436543654365365434, 0.000001, 0.46,
              0.516, 0.800000000000000000000000003]
        self.assertEqual(max_integer(t6), 0.800000000000000000000000003)
        ll0 = [[]]
        self.assertEqual(max_integer(ll0), [])
        tt0 = ((),)
        self.assertEqual(max_integer(tt0), ())
        ll1 = [[5], [4], [100], [3]]
        self.assertEqual(max_integer(ll1), [100])
        tl1 = ([5], [4], [100], [3])
        self.assertEqual(max_integer(tl1), [100])
        tt1 = ((5,), (4,), (100,), (3,))
        self.assertEqual(max_integer(tt1), (100,))
        lt1 = [(5,), (4,), (100,), (3,)]
        self.assertEqual(max_integer(lt1), (100,))
        ll1 = [[5, 3], [4, 800], [100, 2], [3]]
        self.assertEqual(max_integer(ll1), [100, 2])
        tl1 = ([5, 3], [4, 800], [100, 2], [3])
        self.assertEqual(max_integer(tl1), [100, 2])
        tt1 = ((5,), (4,), (100,), (3,))
        self.assertEqual(max_integer(tt1), (100,))
        lt1 = [(5,), (4,), (100,), (3,)]
        self.assertEqual(max_integer(lt1), (100,))
        lll0 = [[[]]]
        self.assertEqual(max_integer(lll0), [[]])
        ttt0 = (((),),)
        self.assertEqual(max_integer(ttt0), ((),))
        self.assertEqual(max_integer("abc!"), "c")
        self.assertEqual(max_integer("abC!"), "b")
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer({}), None)

    def test_types(self):
        """Tests for TypeError exceptions"""
        self.assertRaises(TypeError, max_integer, 6)
        self.assertRaises(TypeError, max_integer, TypeError())
        self.assertRaises(TypeError, max_integer, unittest.TestCase())
        x = unittest.TestCase()
        y = unittest.TestCase()
        self.assertRaises(TypeError, max_integer, [x, y])
        self.assertRaises(TypeError, max_integer, [1, "abc"])
        self.assertRaises(TypeError, max_integer, [1, [2, 3]])
        self.assertRaises(TypeError, max_integer, 3, 2, "x")
        self.assertRaises(TypeError, max_integer, None)
        pass

    def test_indexing(self):
        """Tests for index and key errors"""
        self.assertRaises(KeyError, max_integer, {"aa": 32, 25: 52})

    def test_docs(self):
        """Checks the presence of doc strings"""
        s = __import__('6-max_integer').__doc__
        self.assertTrue(len(s) > 1)
        s = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(s) > 1)
    pass
