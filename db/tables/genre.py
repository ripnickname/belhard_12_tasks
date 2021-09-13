from sqlalchemy import Column, Integer, String

from ..base import Base


class Genre(Base):
    __tablename__ = "genres"

    id = Column(String(20), primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)