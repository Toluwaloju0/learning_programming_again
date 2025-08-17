#!/usr/bin/python3

import sqlalchemy
import sys

from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound


if __name__ == "__main__":
    uname, pword, dbname, stname = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    session = Session(engine)
    try:
        state = session.execute(select(State.id).where(State.name.like(stname))).one()
        print(f"{state.id}")
    except NoResultFound:
        print("Not Found")
    finally:
        session.close()
