#!/usr/bin/python3
"""Unittests for Place class"""

import unittest
from models import place
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for Place Class"""

    def test_instantiation(self):
        """check for instance """
        place1 = Place()
        self.assertIsInstance(place1, Place)


    def test_attributes(self):
        self.assertTrue(hasattr(Place, "email"))
        self.assertIsInstance(Place.email, str)
        self.assertTrue(hasattr(Place, "password"))
        self.assertIsInstance(Place.password, str)
        self.assertTrue(hasattr(Place, "first_name"))
        self.assertIsInstance(Place.first_name, str)
        self.assertTrue(hasattr(Place, "last_name"))
        self.assertIsInstance(Place.last_name, str)


    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(place.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Place.__doc__) > 0)

    def test_method_doc(self):
        """ check for method documentation """
        for func in dir(Place):
            self.assertTrue(len(func.__doc__) > 0)
