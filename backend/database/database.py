# database/database.py
from sqlalchemy import create_engine

# Using SQLite for MVP; replace with your database URL if needed.
engine = create_engine("sqlite:///./eagleeye.db", echo=True)
