import requests

BASE_URL = "http://localhost:5000"

def test_home():
    res = requests.get(f"{BASE_URL}/")
    assert res.status_code == 200
    assert res.json()["message"] == "Hello World!"

def test_get_items():
    res = requests.get(f"{BASE_URL}/items")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_create_item():
    new_item = {"name": "test item"}

    res = requests.post(f"{BASE_URL}/items", json=new_item)
    assert res.status_code == 201

    data = res.json()
    assert data["message"] == "Item added"