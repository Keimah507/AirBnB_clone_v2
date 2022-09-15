#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = Column(String(60), nullable=False)
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete_orphan')
    else:
        @property
        def cities(self):
            """Getter attr in case of file storage"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
