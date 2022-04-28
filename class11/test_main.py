from fastapi.testclient import TestClient

from main import app

client = TestClient(app)



def test_create_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }


def test_create_item_fails_on_wrong_header():
    response = client.post(
        "/items/",
        headers={"X-Token": "wrong header"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 400
    assert response.json().get("detail") == "Invalid X-Token header"

def test_create_item_fails_on_item_exists():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foo", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 400
    assert response.json().get("detail") == "Item already exists"
