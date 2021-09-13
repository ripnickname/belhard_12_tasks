from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class CharacterActor(Base):
    __tablename__ = "characters_actors"

    person_id = Column(Integer, ForeignKey("persons.id", ondelete="CASCADE"), nullable=TRUE, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"), nullable=TRUE, primary_key=True)

    person = relationship("Person")
    character = relationship("Character")