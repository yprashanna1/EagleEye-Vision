# database/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Using SQLite for the MVP; the database file will be named 'eagleeye.db'
DATABASE_URL = "sqlite:///./eagleeye.db"

# Create the SQLAlchemy engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Function to get a database session (useful for dependency injection in FastAPI)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
