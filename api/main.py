from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

# load environment variables
from dotenv import load_dotenv
load_dotenv('.env')


from . import models, schemas, crud
from .database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books", response_model=schemas.Book, status_code=status.HTTP_201_CREATED)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    '''
    Creates a new book in the database and returns it
    Returns an error if a book with the same ISBN already exists
    '''
    if crud.get_book_by_isbn(db=db, isbn=book.isbn) is not None:
        raise HTTPException(status_code=400, detail="book with this ISBN already exists")

    return crud.create_book(db=db, book=book)


@app.get("/books/{book_id:int}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    '''
    Returns a book by id
    Returns an error if the book is not found
    '''
    book = crud.get_book(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@app.put("/books/{book_id:int}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    '''
    Updates a book in the database by id and returns it
    Returns an error if the book is not found
    Returns an error if a book with the same ISBN already exists (unless it is the same book)
    '''
    if crud.get_book_by_isbn(db=db, isbn=book.isbn, book_id=book_id) is not None:
        raise HTTPException(status_code=400, detail="book with this ISBN already exists")
    
    book = crud.update_book(db=db, book_id=book_id, book=book)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book


@app.delete("/books/{book_id:int}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    '''
    Deletes a book from the database by id and returns it
    Returns an error if the book is not found
    '''
    book = crud.delete_book(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book


@app.get("/books", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    '''
    Returns a list of all books in the database
    '''
    books = crud.get_books(db)
    return books


@app.get("/books/rated", response_model=list[schemas.Book])
def read_books_with_ratings(db: Session = Depends(get_db)):
        '''
        Returns a list of all books in the database that have been rated
        '''
        books = crud.get_books_by_ordered_average_rating(db)
        return books


@app.post("/ratings", response_model=schemas.Rating, status_code=status.HTTP_201_CREATED)
def create_rating_for_book(rating: schemas.RatingCreate, db: Session = Depends(get_db)):
    '''
    Creates a new rating in the database and returns it
    Returns an error if the user has already rated the book
    Returns an error if the book is not found
    '''
    if crud.get_rating_by_book_and_user(db=db, book_id=rating.book_id, user_name=rating.user_name) is not None:
        raise HTTPException(status_code=400, detail="The user has already rated this book")
    
    if crud.get_book(db=db, book_id=rating.book_id) is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return crud.create_rating(db=db, rating=rating)


@app.get("/ratings/{book_id:int}", response_model=list[schemas.Rating])
def read_ratings_for_book(book_id: int, db: Session = Depends(get_db)):
        '''
        Returns a list of all ratings for a book
        Returns an error if the book is not found
        '''
        if crud.get_book(db=db, book_id=book_id) is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        ratings = crud.get_ratings_by_book(db=db, book_id=book_id)
        return ratings