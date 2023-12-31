from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
# load environment variable DB_URL from .env file if it exists else use sqlite
SQLALCHEMY_DATABASE_URL = os.environ.get('DB_URL', 'sqlite:///./sql_app.db')

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
