# services/video_service.py

def process_video(file_path: str):
    """
    Dummy function to process a video file.
    Calls the detection model to get detections.
    """
    from models.detection_model import detect_objects
    detections = detect_objects(file_path)
    return detections
