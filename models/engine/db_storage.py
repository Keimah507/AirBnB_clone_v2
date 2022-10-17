#!usr/bin/python3
"""This is the database storage class for AirBnB_clone"""
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel, Base
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Database engine for file storage"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns dictionary of all objects depending of class name
        (argument=cls)"""
        if cls:
            objs = self.__session.query(self.classes()[cls])
        else:
            objs = self.__session.query(State).all()
            objs += self.__session.query(City).all()
            objs += self.__session.query(User).all()
            objs += self.__session.query(Place).all()
            objs += self.__session.query(Amenity).all()
            objs += self.__session.query(Review).all()

        dic = {}
        for obj in objs:
            k = '{}.{}'.format(type(obj).__name__, obj.id)
            dic[k] = obj
        return dic

    def new(self, obj):
        """Adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes database session"""
        self.__session.commit()

    def __delete__(self, obj=None):
        """Delete obj from current database session if obj is not None"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create the current database session (self.__session)
        from the engine (self.__engine) by using a sessionmaker"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.place import Place
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__engine,
                                      expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """Removes the session"""
        self.__session.close()

    def classes(self):
        """Returns a dictionary of valid classes and their attributes"""
        from models.base_model import BaseModel
        from models.city import City
        from models.state import State
        from models.amenity import Amenity
        from models.user import User
        from models.review import Review
        from models.place import Place

        classes = {"Basemodel": BaseModel,
                   "User": User,
                   "State": State,
                   "Review": Review,
                   "Place": Place,
                   "City": City,
                   "Amenity": Amenity}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname"""
        attributes = {
            "Basemodel":
                {
                    "id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
            "User":
                {"email": str,
                 "password": str,
                 "first_name": str,
                 "last_name": str},
            "State":
                {"name": str},
            "City":
                {"state_id": str,
                 "name": str},
            "Amenity":
                {"name": str},
            "Place":
                {"city_id": str,
                 "user_id": str,
                 "name": str,
                 "description": str,
                 "number_rooms": int,
                 "number_bathrooms": int,
                 "max_guest": int,
                 "price_by_night": int,
                 "latitude": float,
                 "longitude": float,
                 "amenity_ids": list},
            "Review":
                {"place_id": str,
                 "user_id": str,
                 "text": str}
        }
        return attributes
