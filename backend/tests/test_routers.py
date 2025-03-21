# tests/test_routers.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_video_router_test_endpoint():
    response = client.get("/api/video/test")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Video API is working!"
