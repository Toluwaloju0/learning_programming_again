#!/usr/bin/python3

import sys

from model_state import Base, State
from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    uname, pword, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(f"mysql+mysqldb://{uname}:{pword}@localhost/{dbname}", pool_pre_ping=True)
    session = Session(engine)

    state = session.execute(select(State).where(State.id == 2)).scalar_one()

    state.name = "New Mexo"
    session.commit()
