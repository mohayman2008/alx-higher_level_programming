#!/usr/bin/python3
"""The module ontains the definition of the State class and
an instance 'Base = declarative_base()'"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Definition of the State class and its relation in the database"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
