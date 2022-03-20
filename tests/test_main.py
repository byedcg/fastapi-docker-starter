from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_background_task():
    response = client.post("/background/task/hi")
    assert response.status_code == 202
    assert response.json() == {"message": "Notification will be sent in the background"}
