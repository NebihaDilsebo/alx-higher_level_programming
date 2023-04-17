#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
author:nebiha"""
import sys
import unittest
import inspect
import io
import pep8
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """class for testing Rectangle class"""

    @classmethod
    def setupclass(cls):
        """
        Sets up class method"""
        cls.setup = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_pep8_conformance_rectangle(self):
        "test to PEP8"""
        pep8style = pep8.StyleGuide(quit=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 1,
                "Found code style errors (and warnings).")

    def test_module_docstring(self):
            """test for the existence of docstring"""
            self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
            """test for the exisrence of class docstring documentation"""
            self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """test for existence of docstring documentation method"""
        self.assertTrue(len(func[1].__doc__) >= 1)

    """def test_wrong_inputted_values(self):
        test for negative and zero values
        """
        with self.assertRaises(ValueError):
            R = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            R = Rectangle(-4, -5)
        with self.assertRaises(ValueError):
            R = Rectangle(1, 1, -2, -2)
        with self.assertRaises(TypeError):
            R = Rectangle()
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_inputted_types(self):
        """different types of arguments"""
        with self.assertRaises(TypeError):
            R = Rectangle('width', 'height')
        with self.assertRaises(TypeError):
            R = Rectangle(2.4,1.3)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 'x values', 'y values')
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 2.4, 1.3)
        with self.assertRaises(TypeError):
            R = Rectangle(True, False)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, True, False)
        with self.assertRaises(TypeError):
            R = Rectangle([1, 1], 2, 3, 4)
        with self.assertRaises(TypeError):
            R = Rectangle((1, 2),'x value', 'y value')
        with self.assertRaises(TypeError):
            R = Rectangle({1: 3, 2: 4}, 5, 6)

    def test_area(self):
        """ test for area method"""
        R = Rectangle(10, 10)
        self.assertEqual(R.area(), 100)
        with self.assertRaises(TypeError):
            A = R.area(1)

    def test_Normal_values(self):
        """normal values just for width and height"""
        R1 = Rectangle(1, 2)
        R2 = Rectangle(1, 2, 3)
        R3 = Rectangle(1, 2, 3, 4)
        R4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual([R1.width, R1.height, R1.x, R1.y, R1.id],
                         [1, 2, 0, 0, 1])
        self.assertEqual([R1.width, R1.height, R1.x, R1.y, R1.id],
                         [1, 2, 0, 0, 1])
        self.assertEqual([R1.width, R1.height, R1.x, R1.y, R1.id],
                         [1, 2, 0, 0, 1])
        self.assertEqual([R1.width, R1.height, R1.x, R1.y, R1.id],
                         [1, 2, 0, 0, 1])
