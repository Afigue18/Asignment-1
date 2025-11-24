from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_sheep():
    response = client.get("/sheep/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():
    new_sheep_data = {
        "id": 7,
        "name": "Bab",
        "breed": "Babydoll",
        "sex": "ram"
    }

    response = client.post("/sheep", json=new_sheep_data)

    assert response.status_code == 201

    sheep_test = response.json()
    assert sheep_test["id"] == new_sheep_data["id"]
    assert sheep_test["name"] == new_sheep_data["name"]
    assert sheep_test["breed"] == new_sheep_data["breed"]
    assert sheep_test["sex"] == new_sheep_data["sex"]
    sheep_id = sheep_test["id"]

    retrieve_response = client.get(f"/sheep/{sheep_id}")

    assert retrieve_response.status_code == 200
    retrieved_sheep = retrieve_response.json()
    assert retrieved_sheep == sheep_test
    assert retrieved_sheep["name"] == "Bab"


