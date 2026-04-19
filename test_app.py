import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["message"] == "Hello World!"

def test_get_items(client):
    res = client.get("/items")
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_create_item(client):
    res = client.post("/items", json={"name": "test item"})
    assert res.status_code == 201
    data = res.get_json()
    assert data["message"] == "Item added"