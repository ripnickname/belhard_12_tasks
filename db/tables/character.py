from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    comment = Column(String(100), nullable=True)
    film_id = Column(Integer, ForeignKey("films.id"), nullable=False)

    film = relationship("Film")
