from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..base import Base


class User(Base):
    __tablename__ = "users"

    login = Column(String(20), primary_key=True)
    password = Column(String(45), nullable=False)
    person_id = Column(Integer, ForeignKey("persons.id"), nullable=False)
    user_type_id = Column(String(20),
                          ForeignKey("user_types.id", onupdate="CASCADE", ondelete="CASCADE"), nullable=False)

    person = relationship("Person")
    user_type = relationship("UserType")

    favorite_film = relationship("Film",
                                 secondary='user_favorite_films',
                                 cascade="all, delete",
                                 passive_deletes=True)
