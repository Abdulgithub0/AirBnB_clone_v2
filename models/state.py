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
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """
            cities returns the list of City instances
            with state_id equals to current state.id
            """
            from models import storage
            from models.city import City
            # calling the storage.all() to get all City instans in file.json
            all_cities = storage.all(City)
            cities = []
            # check if return value of all() is not an empty dict
            if (all_cities):
                v = all_cities.values()
                # get all City instances with state_id == curr State instan id
                cities = list(filter(lambda c: self.id == c.state_id, v))
            return cities
