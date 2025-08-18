#!/usr/bin/python3

from relationship_city import City
from relationship_state import Base
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}", pool_pre_ping=True)
    session = Session(engine)

    for city in session.scalars(select(City).order_by(City.id)).all():
        print(f"{city.id}: {city.name} -> {city.state.name}")