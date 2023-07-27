from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os

postgres_username = os.environ.get('POSTGRES_USERNAME', 'user')
postgres_password = os.environ.get('POSTGRES_PASSWORD', 'password')
postgres_server = os.environ.get('POSTGRES_SERVER', 'localhost')
postgres_db = os.environ.get('POSTGRES_DB', 'db')

SQLALCHEMY_DATABASE_URL = f"postgresql://{postgres_username}:{postgres_password}@{postgres_server}/{postgres_db}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
