#!/usr/bin/python3

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String
from typing import List

class Base(DeclarativeBase):
    pass

class State(Base):
    """ the class which maps to the state table in the database"""

    __tablename__ = "states"

    id: Mapped[int] = mapped_column( primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)

    cities: Mapped[List["City"]] = relationship(back_populates="state", cascade="delete, delete-orphan")
