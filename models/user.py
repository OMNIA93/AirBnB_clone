#!/usr/bin/python3
"""module for user"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel
    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name of the user
        last_name (str): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
