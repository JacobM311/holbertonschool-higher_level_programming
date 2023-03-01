#!/usr/bin/python3
"""List both states and cities
"""
import sys
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state_names = []
    for state in session.query(State).order_by(State.id).all():
        state_names.append(state.name)
    for thing in session.query(City).order_by(City.id).all():
        print("{}: ({}) {}".format(state_names[thing.state_id - 1],
                                   thing.id, thing.name))
    session.close()
