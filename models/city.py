#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.state import State

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        # mapping class City to it responding cities table in db storage engine
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        state = relationship("State", back_populates="cities", cascade="all, delete")
        places = relationship("Place", back_populates="cities", cascade="all, delete-orphan")
    else: # storage_type is filestorage
        state_id = ""
        name = ""
