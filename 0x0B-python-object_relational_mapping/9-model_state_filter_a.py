#!/usr/bin/python3
"""List all state objects from hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
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
    block = []
    substring = "a"
    for state in session.query(State).order_by(State.id).all():
        block.append("{}: {}".format(state.id, state.name))
    for i in block:
        if substring in i:
            print(i)
    session.close()