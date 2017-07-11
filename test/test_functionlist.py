# -*- coding: utf-8 -*-
"""
This module tests the functionlist module.

Run it like so:

coquery$ python -m test.test_functionlist

"""

from __future__ import unicode_literals

import unittest

from coquery.functionlist import FunctionList
from coquery.functions import Function


class TestFunctionList(unittest.TestCase):
    def test_get_list(self):
        func1 = Function(columns=["col1", "col2"], value="x")
        func2 = Function(columns=["col3", "col4"], value="y")

        f_list = FunctionList([func1, func2])
        self.assertListEqual(f_list.get_list(), [func1, func2])

    def test_set_list(self):
        func1 = Function(columns=["col1", "col2"], value="x")
        func2 = Function(columns=["col3", "col4"], value="y")

        f_list = FunctionList()
        self.assertListEqual(f_list.get_list(), [])
        f_list.set_list([func1, func2])
        self.assertListEqual(f_list.get_list(), [func1, func2])

    def test_find_function(self):
        func1 = Function(columns=["col1", "col2"], value="x")
        func2 = Function(columns=["col3", "col4"], value="y")
        func3 = Function(columns=["col5", "col6"], value="z")

        f_list = FunctionList([func1, func2, func3])
        self.assertEqual(f_list.find_function(func1.get_id()), func1)
        self.assertEqual(f_list.find_function(func2.get_id()), func2)
        self.assertEqual(f_list.find_function(func3.get_id()), func3)

    def test_find_function_invalid(self):
        func1 = Function(columns=["col1", "col2"], value="x")
        func2 = Function(columns=["col3", "col4"], value="y")
        func3 = Function(columns=["col5", "col6"], value="z")

        f_list = FunctionList([func1, func3])
        self.assertEqual(f_list.find_function(func1.get_id()), func1)
        self.assertEqual(f_list.find_function(func2.get_id()), None)
        self.assertEqual(f_list.find_function(func3.get_id()), func3)

    def test_add_function(self):
        func1 = Function(columns=["col1", "col2"], value="x")
        func2 = Function(columns=["col3", "col4"], value="y")
        func3 = Function(columns=["col5", "col6"], value="z")

        f_list = FunctionList([])

        f_list.add_function(func1)
        self.assertEqual(f_list.get_list(), [func1])

        f_list.add_function(func2)
        self.assertEqual(f_list.get_list(), [func1, func2])

        f_list.add_function(func3)
        self.assertEqual(f_list.get_list(), [func1, func2, func3])

    def test_has_function(self):
        func1 = Function(columns=["col1", "col2"], value="x")
        func2 = Function(columns=["col3", "col4"], value="y")
        func3 = Function(columns=["col5", "col6"], value="z")

        f_list = FunctionList([func1, func3])

        self.assertTrue(f_list.has_function(func1))
        self.assertFalse(f_list.has_function(func2))
        self.assertTrue(f_list.has_function(func3))

    def test_remove_function(self):
        func1 = Function(columns=["col1", "col2"], value="x")
        func2 = Function(columns=["col3", "col4"], value="y")
        func3 = Function(columns=["col5", "col6"], value="z")

        f_list = FunctionList([func1, func2, func3])

        f_list.remove_function(func2)
        self.assertListEqual(f_list.get_list(), [func1, func3])

        f_list.remove_function(func3)
        self.assertListEqual(f_list.get_list(), [func1])

        f_list.remove_function(func1)
        self.assertListEqual(f_list.get_list(), [])

    def test_replace_function(self):
        func1 = Function(columns=["col1", "col2"], value="x")
        func2 = Function(columns=[func1.get_id()], value="y")
        func3 = Function(columns=["col5", "col6"], value="z")

        f_list = FunctionList([func1, func2])

        f_list.replace_function(func1, func3)
        self.assertListEqual(f_list.get_list(), [func3, func2])
        self.assertEqual(
            f_list.find_function(func2.get_id()).columns,
            [func3.get_id()])

    def test_lapply(self):
        pass


def main():
    suite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestFunctionList),
        ])
    unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    main()