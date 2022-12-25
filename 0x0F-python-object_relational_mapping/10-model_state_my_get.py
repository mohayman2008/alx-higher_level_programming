#!/usr/bin/python3
"""Lists the State object with the name passed as argument
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
    state = session.query(State).filter(State.name == argv[4])
    state = state.scalar()
    if state is None or state.name != argv[4]:
        print("Not found")
    else:
        print(state.id)
