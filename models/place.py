#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.user import User

# declaring table in sqlalchemy expression syntax to represent many-many
metadata = Base.metadata

if (getenv("HBNB_TYPE_STORAGE") == "db"):
    place_amenity = Table("place_amenity", metadata,
                        Column("place_id", String(60), ForeignKey("places.id"), nullable=False, primary_key=True),
                        Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)
            )



class Place(BaseModel, Base):
    """ A place to stay for ever """
    __tablename__ = "places"
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        # __tablename__ = "places"
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
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenities")
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

        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            from models import storage
            am_instan = storage(Amenity).values()
            return (list(filter(lambda am: am.id in self.amenity_ids, am_instan)))
        @amenities.setter
        def amenities(self, obj):
            """
            Setter attribute amenities that handles append method for
            adding an Amenity.id to the attribute amenity_ids.
            """
            if (obj["__class__"] == "Amenity"):
                self.amenity_ids.append(obj.id)
                
