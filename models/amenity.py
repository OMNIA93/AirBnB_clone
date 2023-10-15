#!/usr/bin/python3
"""module for amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    amenity class that inherit from BaseModel
    Attributes:
        name (str): name of the amenity
    """
    name = ""
