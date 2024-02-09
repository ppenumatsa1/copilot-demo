from fastapi.testclient import TestClient
from main import app  # replace with the actual name of your FastAPI app file
import pytest

# Create a TestClient instance
client = TestClient(app)

# Define a sample Todo for testing
sample_todo = {"id": 1, "task": "Test task", "completed": False}

# Test creating a new Todo


def test_create_todo():
    response = client.post("/todo/", json=sample_todo)
    assert response.status_code == 200
    assert response.json() == sample_todo

# Test reading all Todos


def test_read_todos():
    response = client.get("/todo/")
    assert response.status_code == 200
    assert sample_todo in response.json()

# Test reading a specific Todo by ID


def test_read_todo():
    response = client.get(f"/todo/{sample_todo['id']}")
    assert response.status_code == 200
    assert response.json() == sample_todo

# Test updating a specific Todo by ID


def test_update_todo():
    updated_todo = {**sample_todo,
                    "task": "Updated test task", "completed": True}
    response = client.put(f"/todo/{sample_todo['id']}", json=updated_todo)
    assert response.status_code == 200
    assert response.json() == updated_todo

# Test deleting a specific Todo by ID


def test_delete_todo():
    response = client.delete(f"/todo/{sample_todo['id']}")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted"}
