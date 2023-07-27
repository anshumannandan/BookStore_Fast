from pydantic import BaseModel, constr, Field

from datetime import date

class RatingBase(BaseModel):
    book_id: int
    user_name: constr(max_length=255)
    rating: int = Field(..., ge=1, le=5)
    review_text: constr(max_length=500)


class RatingCreate(RatingBase):
    pass


class Rating(RatingBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: constr(max_length=255)
    author : constr(max_length=255)
    published_date : date
    isbn : constr(max_length=13, regex=r"^(978|979)\d{10}$|^\d{9}[0-9X]$")
    price : float = Field(..., ge=0.0)


class Bookreate(BookBase):
    pass


class Book(BookBase):
    id: int
    ratings: list[Rating] = []

    class Config:
        orm_mode = True