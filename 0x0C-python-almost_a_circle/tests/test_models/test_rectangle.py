#!/usr/bin/python3
""" Module Unittest for Rectangle"""

import pep8
from unittest import TestCase
from models import rectangle
from models.base import Base
import inspect
import json
import sys
from io import StringIO

Rectangle = rectangle.Rectangle


class TestRectangle(TestCase):
    """ test class Rectangle """

    def test_A_pep8_conformance(self):
        """Test that we conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py',
                                        'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Rectangle.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Rectangle):
            self.assertTrue(len(func.__doc__) > 0)

    def setUp(self):
        """Method to set the start point"""
        self.r1 = Rectangle(10, 8, 4, 2, 1)
        sys.stdout = StringIO()

    def tearDown(self):
        """Clean everything up after running setup"""
        sys.stdout = sys.__stdout__

    def test_B__init__(self):
        """ Test's for init method """
        r1 = Rectangle(1, 2)
        r2 = Rectangle(1, 2, 3)
        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.y, 4)

    def test_C_typeError(self):
        """ test width, height, x and y are type integers """

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("1", 2)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "2")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 2, "3")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 2, 3, "4")
