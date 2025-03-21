# tests/test_models.py
def test_detection_model():
    from models.detection_model import detect_objects
    result = detect_objects("dummy")
    assert isinstance(result, list)
