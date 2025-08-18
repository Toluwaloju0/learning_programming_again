#!/usr/bin/python3

from model_state import Base, State
from model_city import City
from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    session = Session(engine)

    for row in session.execute(select(City.id, City.name, State.name).join(State).order_by(City.id)).all():
        print(f"{row[2]}: ({row[0]}) {row[1]}")
