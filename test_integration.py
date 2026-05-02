import requests

BASE_URL = "http://localhost:5000"


def reset_items():
    """Reset l'état de l'API pour éviter les effets de bord entre tests"""
    requests.delete(f"{BASE_URL}/items")


def test_home():
    res = requests.get(f"{BASE_URL}/")
    assert res.status_code == 200
    assert res.json()["message"] == "Hello World!"


def test_get_items():
    reset_items()

    res = requests.get(f"{BASE_URL}/items")
    assert res.status_code == 200
    assert isinstance(res.json(), list)
    assert res.json() == []


def test_create_item():
    reset_items()

    res = requests.post(f"{BASE_URL}/items", json={"name": "test item"})
    assert res.status_code == 201

    data = res.json()
    assert data["message"] == "Item added"
    assert data["item"]["name"] == "test item"


def test_delete_items():
    reset_items()

    # ajouter un item
    requests.post(f"{BASE_URL}/items", json={"name": "to delete"})

    # supprimer
    res = requests.delete(f"{BASE_URL}/items")
    assert res.status_code == 200

    # vérifier que la liste est vide
    res = requests.get(f"{BASE_URL}/items")
    assert res.json() == []