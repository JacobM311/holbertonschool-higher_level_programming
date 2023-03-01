#!/usr/bin/python3
"""Delete all rows containing a
"""
import sys
from sqlalchemy import create_engine, delete
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
    stmt = session.query(State).filter(State.name.contains("a"))
    stmt.delete(synchronize_session='fetch')
    session.commit()
    session.close()
