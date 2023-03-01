#!/usr/bin/python3
"""Update name of state
"""
import sys
from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    a_state = session.query(State).filter(State.id == 2).one()
    a_state.name = "New Mexico"
    session.commit()
    session.close()
