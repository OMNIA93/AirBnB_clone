#!/usr/bin/python3
"""module for city class"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    city class that inherit from BaseModel
    Attributes:
        name (str): name of the city
    """
    name = ""
