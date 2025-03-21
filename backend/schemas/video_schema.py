# schemas/video_schema.py
from pydantic import BaseModel

class VideoInput(BaseModel):
    stream_url: str
    timestamp: str
