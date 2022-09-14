#!/usr/bin/python3
"""Database storage engine"""


import models
from models.base_model import Base
from os import getenv
from sqlalchemy import create_engine
from models import (Amenity,City,Place,Review,State,User, BaseModel)
from sqlalchemy.orm import sessionmaker, scoped_session



class DBStorage:
    """DBStorage class definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes DBStorage"""
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV", "none")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(user, password, host, database), pool_pre_ping=True)
        
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries current database session"""
        objs_dict = {}
        if cls:
            objects = self.__session.query(models.classes[cls]).all()
            for obj in objects:
                objs_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        else:
            for k, v in models.classes.items():
                if k != "BaseModel":
                    objs = self.__session.query(v).all()
                    for obj in objs:
                        objs_dict[f"{obj.__class__.__name__}.{obj.id}"] = obj
        # TODO
        return objs_dict

    def new(self, obj):
        """Adds obj to current db session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Commit all changes of current database session"""
        self.__session = Base.metadata.create_all(self.__engine)
        factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(factory)
        self.__session = Session()

    def close(self):
        """Remove private session attribute"""
        self.__session.close()
