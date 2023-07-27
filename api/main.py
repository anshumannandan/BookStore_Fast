from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session


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


@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):

    if crud.get_book_by_isbn(db=db, isbn=book.isbn) is not None:
        raise HTTPException(status_code=400, detail="book with this ISBN already exists")

    return crud.create_book(db=db, book=book)


@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):

    book = crud.get_book(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):

    if crud.get_book_by_isbn(db=db, isbn=book.isbn, book_id=book_id) is not None:
        raise HTTPException(status_code=400, detail="book with this ISBN already exists")
    
    book = crud.update_book(db=db, book_id=book_id, book=book)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book


@app.delete("/books/{book_id}", response_model=schemas.Book)
def delete_book(book_id: int, db: Session = Depends(get_db)):

    book = crud.delete_book(db=db, book_id=book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book


@app.get("/books", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):

    books = crud.get_books(db)
    return books


@app.post("/ratings", response_model=schemas.Rating)
def create_rating_for_book(rating: schemas.RatingCreate, db: Session = Depends(get_db)):

    if crud.get_rating_by_book_and_user(db=db, book_id=rating.book_id, user_name=rating.user_name) is not None:
        raise HTTPException(status_code=400, detail="The user has already rated this book")
    
    if crud.get_book(db=db, book_id=rating.book_id) is None:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return crud.create_rating(db=db, rating=rating)


@app.get("/ratings/{book_id}", response_model=list[schemas.Rating])
def read_ratings_for_book(book_id: int, db: Session = Depends(get_db)):
        
        if crud.get_book(db=db, book_id=book_id) is None:
            raise HTTPException(status_code=404, detail="Book not found")
        
        ratings = crud.get_ratings_by_book(db=db, book_id=book_id)
        return ratings