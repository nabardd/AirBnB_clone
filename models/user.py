#!/usr/bin/env python3

from models import BaseModel

""" User Representation """

class User(BaseModel):
    """Object representation of a User"""

    def __init__(
            self, email="", password="",
            first_name="", last_name=""):
        
        """
        Initializing User object

        Args:
            email (str): user's email
            password (str): user's password
            first_name (str): user's first name
            last_name (str): user's last name
        """

        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""