# services/video_service.py

def process_video(file_path: str):
    """
    Processes the video file using the detection model.
    For the MVP, we process just one frame and return dummy detections.
    """
    from models.detection_model import detect_objects
    
    # Call the dummy detection function
    detections = detect_objects(file_path)
    return detections
