#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import os
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class_objects = (User, State, City, Amenity, Place, Review)


class DBStorage:
    """This class manages storage of hbnb models in a SQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """This class manages storage of hbnb models in a SQL database"""
        user = os.getenv('HBNB_MYSQL_USER')
        pword = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db_name = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        connection_url = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
                user, pword, host, db_name)

        DBStorage.__engine = create_engine(
                connection_url, pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        dict_obj = dict()
        if cls is None:
            for class_s in class_objects:
                obj_query = self.__session.query(class_s)
                for obj in obj_query.all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    dict_obj[key] = obj
        else:
            obj_query = self.__session.query(cls)
            for obj in obj_query.all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                dict_obj[key] = obj
        return dict_obj

    def new(self, obj):
        """Adds new object to storage database"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as ex:
                self.__session.rollback()
                raise ex

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """Loads storage database"""
        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(SessionFactory)()

    def delete(self, obj=None):
        """Removes an object from the storage database"""
        if obj is not None:
            self.__session.query(type(obj)).filter(
                                    type(obj).id == obj.id).delete(
                                    synchronize_session=False)

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.remove()
