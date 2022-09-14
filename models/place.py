#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

from models.review import Review


place_amenity = Table("place_amenity", Base.metadata, Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False), Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
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
    __tablename__ = "places"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name =Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place", cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False, back_populates="place_amenities")
    else:
        @property
        def reviews(self):
            """Returns reviews for a place (when review.id == place.id)"""
            reviews = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews

        @property
        def amenities(self):
            """Returns amenities belonging to a place"""
            from models import Amenity
            amenity_list = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.place_id == self.id:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity):
            """Adds an amenity to a place"""
            from models import Amenity
            # TODO
            if amenity and isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
