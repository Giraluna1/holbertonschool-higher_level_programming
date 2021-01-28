#!/usr/bin/python3
""" Module Unittest for Rectangle"""

import pep8
from unittest import TestCase
from models.rectangle import Rectangle
from models.base import Base
import inspect
import json


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

    def test_B__init__(self):
        """ Test's for init method """
        rectangle_1 = Rectangle(1, 2)
        self.assertEqual(isinstance(rectangle_1, Base), True)
        self.assertEqual(isinstance(Rectangle(1, 2, 3), Base), True)
        self.assertTrue(isinstance(Rectangle(1, 2, 3, 4), Base))
        self.assertRaises(TypeError, Rectangle, ('1', 2))
        self.assertRaises(TypeError, Rectangle, (1, '2'))
