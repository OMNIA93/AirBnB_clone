#!/usr/bin/python3
"""Unittests for Amenity class"""

import unittest
from models.amenity import Amenity
from models import amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity Class"""

    def test_instantiation(self):
        """check for instance """
        amen1 = Amenity()
        self.assertIsInstance(amen1, Amenity)
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertIsInstance(Amenity.name, str)


    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(amenity.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Amenity.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Amenity):
            self.assertTrue(len(func.__doc__) > 0)
