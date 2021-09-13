from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from ..base import Base


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    birthdate = Column(DateTime, nullable=False)

    user = relationship("User")
