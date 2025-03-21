# routers/user_router.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test_user():
    return {"message": "User API is working!"}
