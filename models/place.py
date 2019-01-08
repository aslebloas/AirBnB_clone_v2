#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models import storage


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

    city_id = Column(String(60), ForeignKey('cities.id', ondelete="CASCADE"))
    user_id = Column(String(60), ForeignKey('users.id', ondelete="CASCADE"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # For DBStorage
    amenities = relationship("Amenity", secondary='place_amenity',
                             viewonly=True, backref='place_amenities')

    # For FileStorage
    reviews = relationship("Review", backref="place",
                           cascade="all, delete, delete-orphan")

    @property
    def reviews(self):
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            reviews = relationship("Review", backref="place",
                           cascade="all, delete, delete-orphan")
        else:
            reviews = []
            for k, v storage.all().items():
                if v['place_id'] == self.id:
                    reviews.append(v)
        return reviews
