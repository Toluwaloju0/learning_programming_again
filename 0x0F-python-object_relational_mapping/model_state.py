#!/usr/bin/python3

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, Integer, String

class Base(DeclarativeBase):
    pass

class State(Base):
    """ the class which maps to the state table in the database"""

    __tablename__ = "states"

    id: Mapped[int] = mapped_column( primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
