#!/usr/bin/python3
"""module for state class"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that inherit from BaseModel
    Attributes:
        name (str): name of the state
    """
    name = ""
