#!/usr/bin/python3
"""Unittests for user class"""

import unittest
from models import user
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases for User Class"""

    def test_instantiation(self):
        """check for instance """
        user1 = User()
        self.assertIsInstance(user1, User)


    def test_attributes(self):
        self.assertTrue(hasattr(User, "email"))
        self.assertIsInstance(User.email, str)
        self.assertTrue(hasattr(User, "password"))
        self.assertIsInstance(User.password, str)
        self.assertTrue(hasattr(User, "first_name"))
        self.assertIsInstance(User.first_name, str)
        self.assertTrue(hasattr(User, "last_name"))
        self.assertIsInstance(User.last_name, str)


    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(user.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(User.__doc__) > 0)

    def test_method_doc(self):
        """ check for method documentation """
        for func in dir(User):
            self.assertTrue(len(func.__doc__) > 0)
