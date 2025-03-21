# routers/video_router.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from models.detection_model import detect_objects

router = APIRouter()

@router.get("/test")
async def test_video():
    return {"message": "Video API is working!"}

@router.post("/detect")
async def detect_video(file: UploadFile = File(...)):
    try:
        # Read the uploaded file
        contents = await file.read()
        # For simplicity, write the file to a temporary file
        temp_file = f"temp_{file.filename}"
        with open(temp_file, "wb") as f:
            f.write(contents)
        # Call the dummy detection function
        detections = detect_objects(temp_file)
        return {"detections": detections}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
