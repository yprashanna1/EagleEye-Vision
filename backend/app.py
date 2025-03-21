# app.py
from fastapi import FastAPI
from routers import video_router, alert_router, user_router

app = FastAPI(title="EagleEye Vision Backend")

# Include our API endpoints
app.include_router(video_router.router, prefix="/api/video")
app.include_router(alert_router.router, prefix="/api/alert")
app.include_router(user_router.router, prefix="/api/user")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
