#!/usr/bin/python3
"""
Module city class
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base
from sqlalchemy.orm import relationship


class City(Base):
    """ This City class inherits from Base """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State')
