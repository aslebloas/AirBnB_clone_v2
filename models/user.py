#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)

    places = relationship("Place",
                          backref="user",
                          cascade="all, delete, delete-orphan")

    review = relationship("Review",
                          backref="user",
                          cascade="all, delete, delete-orphan")
    @property
    def reviews(self):
        """getter for reviews of theis placs
        only for file storage"""
        lst = []
        for k, v in models.storage.all(Review).items():
            if v.user_id == self.id:
                lst += [v]
        return lst
