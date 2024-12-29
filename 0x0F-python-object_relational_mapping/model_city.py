#!/usr/bin/python3
"""
Contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    City class that inherits from Base
    
    Attributes:
        id (int): unique identifier for each city
        name (str): name of the city
        state_id (int): foreign key to states.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
