#!/usr/bin/env python3

from models.base_model import BaseModel

"""Object representation of Amenities"""


class Amenity(BaseModel):
    """Object representation of Amenities"""

    def __init__(self, name=""):
        """
        Constructor for Amenities class

        Args:
            name (str): Amenity name
        """
        self.name = name
