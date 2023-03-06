#!/usr/bin/env python3

from models.base_model import BaseModel

"""Object Representation for Places"""

class Place(BaseModel):
    
    """Class Representation for Places"""

    def __init__(self):

        """
        Initialization for the Place class

        Args:
            city_id (str): The unique id of the city
            user_id (str): The unique id of the user
            name (str): The name of the place
            description (str): The description of the place
            number_rooms (int): The number of rooms in the place
            number_bathrooms (int): The number of bathrooms in the place
            max_guest (int): The maximum number of guests allowed in the place
            price_by_night (float): The price by night for the place
            latitude (float): The latitude of the place
            longitude (float): The longitude of the place
            amenity_ids (list): A list of amenity ids for amenities available.
        """
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0.0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
