#!/usr/bin/python3
"""This module contains the unittests of the Base class"""
import unittest


try:
    import models
    from models import Base
    from models.base import Base
except BaseException as e:
    unittest.TestCase.fail(f"Exception [{e}] raised unexpectedly!")

try:
    suite = __import__("test_models.__init__", fromlist=[None])
except Exception:
    try:
        suite = __import__("__init__")
    except Exception:
        suite = __import__("tests.test_models.__init__", fromlist=[None])


class TestBase(unittest.TestCase, Base):
    """Tests for class Base"""

    def test_Base_id(self):
        """Initialization tests"""
        B, last = (Base, suite.base_count)
        bases = (B(), B(), B(34983458763543), B(), B(3), B(4), B())
        ids = (last + 1, last + 2, 34983458763543, last + 3, 3, 4, last + 4)

        i = 0
        for base in bases:
            self.assertEqual(base.id, ids[i])
            del base
            i += 1
        b5 = Base()
        self.assertEqual(b5.id, last + 5)
        suite.base_count += 5
        pass
    pass
