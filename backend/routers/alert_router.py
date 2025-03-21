# routers/alert_router.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
async def test_alert():
    return {"message": "Alert API is working!"}

@router.get("/verify")
async def verify_alerts():
    """
    Dummy endpoint to return alerts that need human verification.
    In a real scenario, this would query the database for alerts marked as needing verification.
    """
    # Return a dummy list of alerts needing verification.
    alerts = [
        {"id": 1, "message": "Suspicious activity detected", "needs_verification": True},
        {"id": 2, "message": "Potential accident detected", "needs_verification": True}
    ]
    return {"alerts": alerts}
