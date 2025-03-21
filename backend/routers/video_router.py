# routers/video_router.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from services.video_service import process_video
import os

router = APIRouter()

@router.get("/test")
async def test_video():
    """
    Simple GET endpoint to verify the video API.
    """
    return {"message": "Video API is working!"}

@router.post("/detect")
async def detect_video(file: UploadFile = File(...)):
    """
    Accepts a video file upload, processes it using the video service,
    and returns the detection results.
    """
    try:
        # Read the file content from the uploaded file
        contents = await file.read()
        
        # Save the file temporarily in the project directory
        temp_file = f"temp_{file.filename}"
        with open(temp_file, "wb") as f:
            f.write(contents)
        
        # Process the video using our video service
        detections = process_video(temp_file)
        
        # Remove the temporary file after processing
        os.remove(temp_file)
        
        return {"detections": detections}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
