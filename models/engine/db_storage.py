#!/usr/bin/python3

"""Declaration and defintiion of database"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place, place_amenity
from models.review import Review
from models.user import User
from sqlalchemy.orm.scoping import scoped_session

# needed details to create the engine --> separation of concerns principle
if (getenv("HBNB_TYPE_STORAGE") == "db"):
    u = getenv("HBNB_MYSQL_USER")
    p = getenv("HBNB_MYSQL_PWD")
    db = getenv("HBNB_MYSQL_DB")
    h = getenv("HBNB_MYSQL_HOST") + ":3306"
    ser = "mysql+mysqldb"



classes = (City, State, User, Place, Review, Amenity, place_amenity)

class DBStorage:
    """contain all attrs and methods definition for db storage type"""

    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(f"{ser}://{u}:{p}@{h}/{db}",
                                      pool_pre_ping=True)
        # mapping all subclasses of Base to their respective tables
        # Base.metadata.create_all(self.__engine)
        if (u == "test"):
            Base.metadata.drop_all(self.__engine)
        
        # Opening communication interface btw db engine and mysql server
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def all(self, cls=None):
        """return  all objs in current database session"""

        objects = {}
        if not (cls) and cls in classes: # check if cls exist and in list of classes or return every instances in db
            rows = self.__session.query(cls).all() # get all instances of the Class
            for row in rows:
                key = f'{type(row).__name__}.{row["id"]}' # create the key reference to each instance
                objects[key] = row
            return objects
        for cl in classes:
            rws = self.__session.query(cl).all()
            for rw in rws:
                key = f'{type(rw).__name__}.rw.id'
                objects[key] = rw
        return objects

    def new(self, obj):
        """add obj to the current database session"""
        if (obj):
            self.__session.add(obj)
            self.__session.flush()

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if (obj):
            self.__session.delete(obj)
            self.__session.flush()

    def reload(self):
        """create/get all previously tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
        #Base.metadata.create_all(self.__engine)
    

    def close(self):
        """close session"""
        self.__session.commit()
        self.__session.close()
