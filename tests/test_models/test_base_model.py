#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
import os
import sys
from datetime import datetime
from models import base_model
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_uuid(self):
        """unique identifier (UUID) test"""
        
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)


    def test_to_dict(self):
        """ dictionary represntation test"""

        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        self.assertTrue(bm1.__dict__, type(dict))
        self.assertEqual(dict, type(bm1_dict))
        self.assertEqual(bm1.id, bm1_dict["id"])
        self.assertEqual("BaseModel", bm1_dict["__class__"])
        self.assertEqual(bm1.created_at.isoformat(),
                         bm1_dict["created_at"])
        self.assertEqual(bm1.updated_at.isoformat(),
                         bm1_dict["updated_at"])

