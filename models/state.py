#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        # from models.city import City
        # map State to its db table called states
        __tablename__= "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """
            cities returns the list of City instances
            with state_id equals to current state.id
            """
            from models import storage
            # calling the storage.all() to query out all City instances in file.json
            all_cities = storage.all(City)
            cities = []
            if (all_cities): # check if return value of all() is not an empty dict
                v = all_cities.values()
                # filter out all City instances with state_id attr == this curr State instance id
                cities = list(filter(lambda c: self.id == c.state_id, v))
            return cities
        
