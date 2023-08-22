#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """ A place to stay for ever """
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        cities = relationship("City", back_populates="places", cascade="all, delete")
        user = relationship("User", back_populates="places", cascade="all, delete")
        reviews = relationship("Review", back_populates="place", cascade="all, delete-orphan")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
        
        @property
        def reviews(self):
            """
            getter attribute reviews that returns the list of Review
            instances with place_id equals to the current Place.id
            """
            from models import storage
            review_instances = storage.all(Review)
            same_id = []
            for review in review_instances:
                if self.id == review.place_id:
                    same_id.append(review)
            return same_id
