#!/usr/bin/python3
"""This is the state class"""
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities: reference to the City objects related to State
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete, delete-orphan")

    # For FileStorage
