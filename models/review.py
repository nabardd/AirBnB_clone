#!/usr/bin/env python3

from models.base_model import BaseModel

"""Class for reviews"""

class Review(BaseModel):
    """Object representation for reviews"""

    def __init__(self):
        """
        Initialization for the Review class

        Args:
            place_id (str): the unique ID for place reviewed
            user_id (str): the unique ID for user reviewing a place
            text (str): the text of the review
        """
        self.place_id = ""
        self.user_id = ""
        self.text = ""