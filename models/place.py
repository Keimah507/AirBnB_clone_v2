#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import DateTime, Float, Table
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from models.city import City
from models.review import Review
from models.amenity import Amenity

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id',
                                 String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id',
                                 String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        review = relationship('Review', backref='Place',
                              cascade='all, delete_orphan')
        amenities = relationship('Amenity',
                                 secondary='place_amenity',
                                 backref='Place', viewonly=False)
    else:
        @property
        def reviews(self):
            """Getter attribute in case of file storage"""
            return [review for review in models.storage.all(Review)
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """Getter attribute in case of file storage"""
            return [amenity for amenity in models.storage.all(Amenity)
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """Setter method for amenities"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
