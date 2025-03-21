# tests/test_services.py
def test_video_service():
    from services.video_service import process_video
    result = process_video("dummy_file")
    assert isinstance(result, list)
