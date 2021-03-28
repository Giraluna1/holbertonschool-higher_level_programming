#!/usr/bin/python3
"""
Module that improve the class City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """
    This City class inherits from Base
    @id: Integer, unique, can't be null, primary key
    @name : String, not null
    @state_id: Integer, Foreing Key
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State')
