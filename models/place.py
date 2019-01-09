#!/usr/bin/python3
"""This is the place class"""
import os
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import environ as env
import models


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id')),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id')))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # For DBStorage
    __amenities = relationship("Amenity", secondary='place_amenity',
                               viewonly=False, backref='place')

    # For FileStorage
    __reviews = relationship("Review",
                             cascade="all, delete", backref="place")

    @property
    def reviews(self):
        """getter for reviews of theis placs
           only for file storage"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            return self.__reviews
        else:
            lst = []
            for k, v in models.storage.all(Review).items():
                if v.place_id == self.id:
                    lst += [v]
            return lst

    @property
    def amenities(self):
        """getter for amenities of theis placs
           only for file storage"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            return self.__amenities
        else:
            lst = []
            for k, v in models.storage.all(Amenity).items():
                if v.place_id == self.id:
                    lst += [v]
            return lst
