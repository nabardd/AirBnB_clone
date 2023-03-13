#!/usr/bin/env python3

from models.base_model import BaseModel
"""Object Representation of a State"""


class State(BaseModel):
    """Representation of a State"""

    def __init__(self, name) -> None:

        """
        intialize a State instance

        Args:
            name (str): name of the State
        """
        self.name = ""
