#!/usr/bin/env python3

from models.base_model import BaseModel

"""Object Representation of a City"""


class City(BaseModel):
    """Representation of a City"""

    def __init__(self, state_id, name):
        """
        Constructor for City class

        Args:
            state_id (str): it will be the State.id
            name (str): it will be the name of the city
        """
        self.state_id = ""
        self.name = ""
