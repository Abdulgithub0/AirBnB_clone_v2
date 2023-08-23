#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.place import place_amenity
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel, Base):
    """class Amenity mapped to table amenities in db"""
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity", back_populates="amenities")
    else:
        name = ""
