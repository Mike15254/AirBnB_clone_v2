#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.city import City



class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(60), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    else:
        name = ""
        @property
        def cities(self):
            """
            returns the list of City instances with state_id equals to the current State.id
            """
            cities = []
            for city in models.storage.all(City).values():
                if self.id == city.id:
                    cities.append(city)
            return cities
