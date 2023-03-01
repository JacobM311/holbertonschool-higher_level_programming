#!/usr/bin/python3
"""List state id from arg
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
    block = 0
    substring = "a"
    for state in session.query(State).order_by(State.id).all():
        if sys.argv[4] == state.name:
            block += state.id
    if block < 1:
        print("Not found")
    else:
        print(block)
    session.close()
