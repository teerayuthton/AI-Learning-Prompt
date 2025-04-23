import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

from src.main import app  

client = TestClient(app)

@patch("src.main.client.chat.completions.create")
def test_generate_response_success(mock_create):
    mock_create.return_value.choices = [
        type("Choice", (), {"message": type("Message", (), {"content": "Test response from OpenAI"})})
    ]

    response = client.post("/generate", json={"prompt": "Hello!"})
    assert response.status_code == 200
    assert response.json() == {"response": "Test response from OpenAI"}

@patch("src.main.client.chat.completions.create")
def test_generate_response_failure(mock_create):
    mock_create.side_effect = Exception("OpenAI API Error")

    response = client.post("/generate", json={"prompt": "Hello!"})
    assert response.status_code == 500
    assert response.json() == {"detail": "Internal Server Error"}

def test_generate_response_invalid_request():
    response = client.post("/generate", json={})
    assert response.status_code == 422  # Validation error from FastAPI/Pydantic
