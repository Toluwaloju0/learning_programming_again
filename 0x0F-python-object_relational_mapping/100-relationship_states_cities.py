#!/usr/bin/python3

from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")
    Base.metadata.create_all(engine)
    session = Session(engine)

    cali = State(name="California")
    san  = City(name="San Francisco")
    cali.cities.append(san)

    session.add_all([cali, san])
    session.commit()
