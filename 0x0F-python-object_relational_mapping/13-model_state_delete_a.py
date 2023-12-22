#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter 'a',
from the database hbtn_0e_6_usa"""
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
    to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for state in to_delete:
        if 'a' in state.name:
            session.delete(state)
    session.commit()
