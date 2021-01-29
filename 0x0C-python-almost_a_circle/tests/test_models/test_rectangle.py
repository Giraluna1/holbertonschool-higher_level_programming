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
        r4 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r3.y, 4)
        self.assertEqual(r4.id, 5)

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

    def test_D_ValueError(self):
        """ Test width, height are greather than cero,
            x and y GreaterEqual than cero
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 2, -3)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 2, 3, -4)

    def test_E_area(self):
        """ Test Area Exists """
        r = Rectangle(1, 2)
        self.assertEqual(r.area(), 2)

    def test_F__str__(self):
        """ Test __str__ exists """
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_G_display_without_x_and_y(self):
        """ Test for method Display exist with diferents cases"""

        r1 = Rectangle(2, 5)
        out1 = "##\n" \
               "##\n" \
               "##\n" \
               "##\n" \
               "##\n"

        r1.display()
        self.assertEqual(sys.stdout.getvalue(), out1)

    def test_H_display_without_y(self):
        """ Test for method Display exist with diferents cases"""

        r2 = Rectangle(2, 2, 3)
        out2 = "   ##\n" \
               "   ##\n"

        r2.display()
        self.assertEqual(sys.stdout.getvalue(), out2)

    def test_I_to_dictionary(self):
        """ Test for method to dictionary exists """

        r1 = Rectangle(10, 2, 1, 9, 19)
        self.assertEqual(r1.to_dictionary(), {'x': 1,
                                              'y': 9, 'id': 19,
                                              'height': 2, 'width': 10})

    def test_J_update(self):
        """ Test for method update """

        r1 = Rectangle(1, 2)
        r1.update(10)
        self.assertEqual(r1.__str__(), "[Rectangle] (10) 0/0 - 1/2")
