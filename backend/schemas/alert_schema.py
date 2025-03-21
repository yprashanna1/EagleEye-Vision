# schemas/alert_schema.py
from pydantic import BaseModel

class Alert(BaseModel):
    message: str
    confidence: float
