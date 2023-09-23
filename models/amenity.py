#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

if (getenv("HBNB_TYPE_STORAGE") == "db"):
    from models.place import place_amenity


class Amenity(BaseModel, Base):
    """class Amenity mapped to table amenities in db"""
    __tablename__ = "amenities"
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity", back_populates="amenities")
    else:
        name = ""
