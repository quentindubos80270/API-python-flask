import pytest
import requests

BASE_URL = "http://localhost:5000"

def test_home():
    res = requests.get(f"{BASE_URL}/")
    assert res.status_code == 200
    assert res.text == "Hello World!"

def test_get_items():
    res = requests.get(f"{BASE_URL}/items")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_create_item():
    res = requests.post(f"{BASE_URL}/items", json={"name": "test item"})
    assert res.status_code == 201
    data = res.json()
    assert data["message"] == "Item added"

def test_delete_items():
    # ajouter un item
    requests.post(f"{BASE_URL}/items", json={"name": "to delete"})

    # supprimer
    res = requests.delete(f"{BASE_URL}/items")
    assert res.status_code == 200

    # vérifier que la liste est vide
    res = requests.get(f"{BASE_URL}/items")
    assert res.json() == []