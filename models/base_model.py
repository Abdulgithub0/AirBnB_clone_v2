#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime
from os import getenv

if (getenv("HBNB_TYPE_STORAGE") != "db"):
    Base = object
else:
    Base = declarative_base()



class BaseModel:
    """A base class for all hbnb models"""

    # Task 6: add new class attrs that will used for db storage only
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)
        updated_at = Column(DateTime(), default=datetime.utcnow(), nullable=False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        if not kwargs:
            # from models import storage cancel out by task 6
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self) this got cancelled out --> by task 6
        else:
            for  key in kwargs.keys():
                if key in  ("updated_at", "created_at"):
                    kwargs[key] = datetime.strptime(kwargs[key],
                                                    '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "__class__":
                    del kwargs[key]
            if not("id" in kwargs.keys()):
                kwargs.update({"updated_at": datetime.now()})
                kwargs.update({"created_at": datetime.now()})
                kwargs.update({"id": str(uuid.uuid4())})
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self) # task 6: move the storage.new() method from BaseModel __init__ to save method
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if "_sa_instance_state" in dictionary.keys():
            del dictionary["_sa_instance_state"]
        return dictionary

    def delete(self):
        """delete the current instance from the storage"""
        from model import storage as delete
        delete.delete(self)
