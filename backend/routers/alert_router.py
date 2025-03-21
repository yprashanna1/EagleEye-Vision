# routers/alert_router.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test_alert():
    return {"message": "Alert API is working!"}