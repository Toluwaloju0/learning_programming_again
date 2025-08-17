#!/usr/bin/python3

import sqlalchemy
import sys

from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session


if __name__ == "__main__":
    uname, pword, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    session = Session(engine)
    for state in session.execute(select(State.id, State.name).where(State.name.like('%a%')).order_by(State.id)).all():
        print(f"{state.id}: {state.name}")

    session.close()
