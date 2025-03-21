# database/init_db.py

from .database import engine
from .models import Base

# Create all tables based on the models defined in models.py
Base.metadata.create_all(bind=engine)
print("Database initialized!")
