#!/usr/bin/python3
"""Unittests for Review class"""

import unittest
from models.review import Review
from models import review


class TestReview(unittest.TestCase):
    """Test cases for Review Class"""

    def test_instantiation(self):
        """check for instance """
        rev1 = Review()
        self.assertIsInstance(rev1, Review)
        self.assertTrue(hasattr(Review, "name"))
        self.assertIsInstance(Review.name, str)


    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(review.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(Review.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(Review):
            self.assertTrue(len(func.__doc__) > 0)
