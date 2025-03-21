# tests/test_models.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_detection_model():
    from models.detection_model import detect_objects
    results = detect_objects("dummy_file")
    assert isinstance(results, list)
    if results:
        detection = results[0]
        assert "object" in detection
        assert "confidence" in detection
        assert "needs_verification" in detection
