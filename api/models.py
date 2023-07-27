from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    published_date = Column(Date)
    isbn = Column(Integer)
    price = Column(Float)

    ratings = relationship("Rating", back_populates="book")


class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    user_name = Column(String)
    rating = Column(Integer)
    review_text = Column(String)

    book = relationship("Book", back_populates="ratings")
