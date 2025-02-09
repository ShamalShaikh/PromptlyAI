from fastapi.testclient import TestClient
import pytest
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

def test_generate_text(client):
    response = client.post(
        "/generate",
        json={
            "prompt": "Test prompt",
            "max_tokens": 50
        }
    )
    assert response.status_code == 200
    assert "text" in response.json() 