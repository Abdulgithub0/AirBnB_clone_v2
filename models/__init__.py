#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == 'db':
    from models.engine.db_storage import DBStorage
    # from models.engine.db_storage import DBStorage
    storage = DBStorage()
    type_s = "db" #-->got circular import issues

else: # from models.engine.file_storage import FileStorage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    # storage.type = "file"
storage.reload()
