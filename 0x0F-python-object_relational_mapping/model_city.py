#!/usr/bin/python3

from model_state import Base
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

class City(Base):
    """ the city class mapped to the city table in the databases"""

    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    state_id: Mapped[int] = mapped_column(ForeignKey("states.id"))
