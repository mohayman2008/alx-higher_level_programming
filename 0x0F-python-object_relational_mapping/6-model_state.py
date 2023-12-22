#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    eng = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(eng, pool_pre_ping=True)
    Base.metadata.create_all(engine)
