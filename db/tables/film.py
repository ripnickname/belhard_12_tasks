from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

from ..base import Base


class Film(Base):
    __tablename__ = "films"

    id = Column(Integer, primary_key=True, autoincrement=True)
    duration = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    release_date = Column(DateTime, nullable=False)
    rating = Column(Float(3, 2), nullable=False)
    person_id = Column(Integer, ForeignKey("persons.id"), nullable=False)

    person = relationship("Person")

    favorite_user = relationship("User",
                                 secondary='user_favorite_films',
                                 cascade="all, delete",
                                 passive_deletes=True)
