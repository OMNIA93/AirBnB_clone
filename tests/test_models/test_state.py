#!/usr/bin/python3
"""Unittests for State class"""

import unittest
from models.state import State
from models import state


class TestState(unittest.TestCase):
    """Test cases for State Class"""

    def test_instantiation(self):
        """check for instance """
        state1 = State()
        self.assertIsInstance(state1, State)


    def test_attributes(self):
        self.assertTrue(hasattr(State, "name"))
        self.assertIsInstance(State.name, str)


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
