from sqlalchemy.orm import Session

from . import models, schemas


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_book_by_isbn(db: Session, isbn: str, book_id: int = None):
    book = db.query(models.Book).filter(models.Book.isbn == isbn).first()
    if book is not None and book.id != book_id:
        return book


def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is not None:
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book


def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is not None:
        db.delete(db_book)
        db.commit()
        return db_book


def get_books(db: Session):
    return db.query(models.Book).all()


def create_rating(db: Session, rating: schemas.RatingCreate):
    db_rating = models.Rating(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating


def get_rating_by_book_and_user(db: Session, book_id: int, user_name: str):
    return db.query(models.Rating).filter(models.Rating.book_id == book_id,
                                          models.Rating.user_name == user_name).first()


def get_ratings_by_book(db: Session, book_id: int):
    return db.query(models.Rating).filter(models.Rating.book_id == book_id).all()