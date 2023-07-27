from fastapi import FastAPI


from dotenv import load_dotenv
load_dotenv('.env')


from . import models
from .database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}