#!/usr/bin/python3
"""Unittests for State class"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State Class"""

    def test_instantiation(self):
        """check for instance """
        self.assertIsInstance(State, State())


    def test_attributes(self):
        self.assertTrue(hasattr(State, "email"))
        self.assertIsInstance(State.email, str)
        self.assertTrue(hasattr(State, "password"))
        self.assertIsInstance(State.password, str)
        self.assertTrue(hasattr(State, "first_name"))
        self.assertIsInstance(State.first_name, str)
        self.assertTrue(hasattr(State, "last_name"))
        self.assertIsInstance(State.last_name, str)


    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(state.__doc__) > 0)

    def test_class_doc(self):
        """ check for class documentation """
        self.assertTrue(len(State.__doc__) > 0)

    def test_method_doc(self):
        """ check for method documentation """
        for func in dir(State):
            self.assertTrue(len(func.__doc__) > 0)
