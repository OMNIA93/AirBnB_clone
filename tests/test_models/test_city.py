#!/usr/bin/python3
"""Unittests for City class"""

import unittest
from models.city import City
from models import city


class TestCity(unittest.TestCase):
    """Test cases for City Class"""

    def test_instantiation(self):
        """check for instance """
        city1 = City()
        self.assertIsInstance(city1, City)
        self.assertTrue(hasattr(City, "name"))
        self.assertIsInstance(City.name, str)


    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(city.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(City.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(City):
            self.assertTrue(len(func.__doc__) > 0)
