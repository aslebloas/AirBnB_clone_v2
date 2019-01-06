#!/usr/bin/python3
"""
Module for DB storage
"""
import os
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBStorage():
    """
    Class DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of a new DBStorage instance"""
        usr = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(usr, pwd, host, db),
            pool_pre_ping=True)
        if (os.getenv('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)
        Base.metadata.create_all(self.__engine)

        self.__session = sessionmaker(bind=engine)()

    def all(self, cls=None):
        """query the current db for all objects
           Args:
               cls: Class name of the object to be queried
        """
        if cls == None:
            results = self.__session.query(
                User, State, City, Amenity, Place, Review).all()
        else:
            results = self.__session.query(cls).all()
        # TODO: this method must return a dictionary
        return dict(results)

    def new(self, obj):
        """Add new object to the current db session
            Args:
                obj: object to be added
        """
        self.__session.add(obj)

    def save(self):
        """Commit all changes to the db session"""
        self.__session.commit()
