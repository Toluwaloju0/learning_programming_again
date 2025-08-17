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
    state = session.execute(select(State.id, State.name).order_by(State.id)).first()
    print(f"{state.id}: {state.name}")

    session.close()
