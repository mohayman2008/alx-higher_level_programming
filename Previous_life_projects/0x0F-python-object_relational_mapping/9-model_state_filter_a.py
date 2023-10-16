#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa"""
from sys import argv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    eng = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    engine = create_engine(eng, pool_pre_ping=True)
    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    query = session.query(State).filter(State.name.like("%a%"))
    query = query.order_by(State.id)
    for state in query.all():
        if 'a' in state.name:
            print(f'{state.id}: {state.name}')
