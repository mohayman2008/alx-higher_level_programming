#!/usr/bin/python3
"""Changes the name of the State object with id = 2 to
New Mexico in the database hbtn_0e_6_usa"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    eng = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(eng, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    to_update = session.query(State).filter(State.id == 2).scalar()
    to_update.name = 'New Mexico'
    session.commit()
