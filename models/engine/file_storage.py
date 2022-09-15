#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
import datetime
from models.base_model import BaseModel,Base
from models.user import  User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            for key, value in self.__objects.items():
                temp[key] = value.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    val = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Removes instance from file"""
        if obj is None:
            pass
        else:
            obj_ref = "{}.{}".format(type(obj).__name__, obj.id)
            if (obj_ref, obj) in self.__objects.items():
                self.__objects.pop(obj_ref, None)
        self.save()

    def close(self):
        """Deserializes JSON file to objects"""
        self.reload()

    def classes(self):
        """Returns a dictionary of valid classes and their references."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def attributes(self):
        """Returns the valid attributes and their types for classname."""
        attributes = {
            "BaseModel":
                {"id": str,
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
