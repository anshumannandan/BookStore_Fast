from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship

from .database import Base


class Book(Base):
    '''
    Book model to store book information
    '''
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255))
    published_date = Column(Date)
    isbn = Column(String(13), 
                  CheckConstraint("isbn ~ '^(978|979)\d{10}$' OR isbn ~ '^\d{9}[0-9X]$'"),
                  unique=True, nullable=False)
    price = Column(Float, CheckConstraint("price >= 0.0"), nullable=False)

    ratings = relationship("Rating", back_populates="book")


class Rating(Base):
    '''
    Rating model to store user ratings and reviews for books
    '''
    __tablename__ = "ratings"
    __table_args__ = (UniqueConstraint('book_id', 'user_name'),)

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    user_name = Column(String(255), nullable=False)
    rating = Column(Integer, CheckConstraint("rating >= 1 AND rating <= 5"), nullable=False)
    review_text = Column(String(500), nullable=False)

    book = relationship("Book", back_populates="ratings")
