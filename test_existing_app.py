from fastapi.testclient import TestClient
from existing import app

client = TestClient(app)


def test_create_todo():
    response = client.post("/todo/", json={"id": 1, "task": "Test task"})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "task": "Test task", "completed": False}


def test_get_todos():
    response = client.get("/todo/")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "task": "Test task", "completed": False}]


def test_get_todo():
    response = client.get("/todo/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "task": "Test task", "completed": False}


def test_update_todo():
    response = client.put(
        "/todo/1", json={"id": 1, "task": "Updated task", "completed": True})
    assert response.status_code == 200
    assert response.json() == {
        "id": 1, "task": "Updated task", "completed": True}


def test_delete_todo():
    response = client.delete("/todo/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted"}
