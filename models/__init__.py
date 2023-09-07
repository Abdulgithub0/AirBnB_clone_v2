#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
s_type = getenv("HBNB_TYPE_STORAGE")

if (s_type == "db"):
        from models.engine.db_storage import DBStorage
        storage = DBStorage()
        type_s = "db" #-->got circular import issues
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    # storage.type = "file"
storage.reload()
