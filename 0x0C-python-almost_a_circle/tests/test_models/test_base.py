#!/usr/bin/python3
""" Module Unittest for base"""

import unittest
import pep8
import inspect


from models.base import Base


class TestBase(unittest.TestCase):
    """ test class Base """
    def test_pep8_conformance(self):
        """Test that we conforms to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py',
                                        'tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test___init__(self):
        """ Test's for init method """

        self.assertTrue(Base.__init__.__doc__)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(7).id, 7)
        self.assertEqual(Base("number").id, "number")
        self.assertEqual(Base().id, 2)

    def test_to_json_string(self):
        """ Test for to_json_string method """

        json_string = Base().to_json_string({"id": 2020, "test": 1})
        self.assertEqual(type(json_string), type("test"))
        self.assertRegex(json_string, "\"id\": 2020")
        self.assertRegex(json_string, "\"test\": 1")

    def test_save_to_file(self):
        """ test for save_to_file method """

        self.assertTrue(Base.save_to_file.__doc__)

    def test_from_json_string(self):
        """ Tests for from_json_string method """

        json_string = Base().to_json_string({"id": 2000, "test": 1})
        self.assertTrue(Base.from_json_string.__doc__)
        say = Base.from_json_string(json_string)
        self.assertEqual(say["id"], 2000)
        self.assertEqual(say["test"], 1)

    def test_create(self):
        """ Tests for create method """

        self.assertTrue(Base.create.__doc__)

    def test_load_from_file(self):
        """ Test's for load_from_file method """

        self.assertTrue(Base.load_from_file.__doc__)

if __name__ == '__main__':
    unittest.main()
