from sqlalchemy import Column, Integer, String, ForeignKey

from ..base import Base


class FilmGenre(Base):
    __tablename__ = "films_genres"

    film_id = Column(Integer, ForeignKey("films.id", ondelete="CASCADE"), primary_key=True)
    genre_id = Column(String(20), ForeignKey("genres.id", ondelete="CASCADE"), primary_key=True)
