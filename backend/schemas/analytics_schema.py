# schemas/analytics_schema.py
from pydantic import BaseModel

class Analytics(BaseModel):
    total_alerts: int
