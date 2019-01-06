#!/usr/bin/python3
"""
Module for DB storage
"""
import os
from models.base_model import Base
from sqlalchemy import create_engine


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
