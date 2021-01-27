#!/usr/bin/python3
""" Module Unittest for base"""

import pep8
from unittest import TestCase
from models.base import Base
import inspect
import json


class TestBase(TestCase):
    """ test class Base """
    def test_A_pep8_conformance(self):
        """Test that we conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(Base.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Base):
            self.assertTrue(len(func.__doc__) > 0)

    def test_B__init__(self):
        """ Test's for init method """

        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(7).id, 7)
        self.assertEqual(Base("number").id, "number")

    def test_C_to_json_string(self):
        """ Test of to json string """
        self.assertTrue(Base.to_json_string(None), [])
        self.assertTrue(Base.to_json_string([]), [])
        self.assertEqual(Base.to_json_string([{'id': 12}]),
                         json.dumps([{'id': 12}]))
        self.assertEqual(Base.to_json_string([{'id': 12}]),
                         json.dumps([{'id': 12}]))

    def test_D_from_json_string(self):
        """ Tetst for from json string """

        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string('[]'), [])
