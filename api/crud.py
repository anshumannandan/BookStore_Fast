from sqlalchemy.orm import Session
from sqlalchemy.sql import func

from . import models, schemas


def create_book(db: Session, book: schemas.BookCreate):
    '''
    Creates a new book in the database
    '''
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: int):
    '''
    Returns a book by id
    '''
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_book_by_isbn(db: Session, isbn: str, book_id: int = None):
    '''
    Returns a book by isbn number
    Book id can be passed to exclude the book with that id from the query
    '''
    book = db.query(models.Book).filter(models.Book.isbn == isbn).first()
    if book is not None and book.id != book_id:
        return book


def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    '''
    Updates a book in the database by id
    '''
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is not None:
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        db.commit()
        db.refresh(db_book)
        return db_book


def delete_book(db: Session, book_id: int):
    '''
    Deletes a book from the database by id
    '''
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book is not None:
        db.delete(db_book)
        db.commit()
        return db_book


def get_books(db: Session):
    '''
    Returns all books in the database
    '''
    return db.query(models.Book).all()


def get_books_by_ordered_average_rating(db: Session):
    '''
    Returns all books in the database ordered by average rating
    If a book has no ratings, it is given a rating of 0
    
    equivalent sql query:
    select * from books
    left join ratings on books.id = ratings.book_id
    group by books.id
    order by coalesce(avg(ratings.rating), 0) desc;
    '''
    return db.query(models.Book).join(models.Rating, isouter=True).group_by(models.Book.id)\
        .order_by(func.coalesce(func.avg(models.Rating.rating), 0).desc()).all()


def create_rating(db: Session, rating: schemas.RatingCreate):
    '''
    Creates a new rating in the database
    '''
    db_rating = models.Rating(**rating.dict())
    db.add(db_rating)
    db.commit()
    db.refresh(db_rating)
    return db_rating


def get_rating_by_book_and_user(db: Session, book_id: int, user_name: str):
    '''
    Returns a rating by book id and user name
    '''
    return db.query(models.Rating).filter(models.Rating.book_id == book_id,
                                          models.Rating.user_name == user_name).first()


def get_ratings_by_book(db: Session, book_id: int):
    '''
    Returns all ratings for a book by book id
    '''
    return db.query(models.Rating).filter(models.Rating.book_id == book_id).all()