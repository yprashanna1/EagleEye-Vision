# database/crud.py

from sqlalchemy.orm import Session
from .models import Alert

def create_alert(db: Session, message: str, confidence: float):
    new_alert = Alert(message=message, confidence=confidence)
    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)
    return new_alert

def get_alerts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Alert).offset(skip).limit(limit).all()
