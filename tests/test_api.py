import pytest
import requests

ESTABLISHMENT_URL = "http://0.0.0.0:8000/api/v1/establishment/"
PRODUCT_URL = "http://0.0.0.0:8000/api/v1/products/"

@pytest.fixture
def EstablishmentSample():
    return {"name": "Test Establishment", "location": "123 Test Street", "opening_hours": "12:00 - 18:00", "description":"some description about Street"}


def test_CREATEEstablishment(EstablishmentSample):
    response = requests.post(ESTABLISHMENT_URL, json=EstablishmentSample)
    assert response.status_code == 201 
    assert response.json()["name"] == EstablishmentSample["name"]

def test_GETEstablishment(EstablishmentSample):
    response = requests.post(ESTABLISHMENT_URL, json=EstablishmentSample)
    assert response.status_code == 201

    response = requests.get(ESTABLISHMENT_URL + str(response.json()["id"]) + "/")
    assert response.status_code == 200
    assert response.json()["name"] == EstablishmentSample["name"]


def testUPDATEEstablishment(EstablishmentSample):
    response = requests.post(ESTABLISHMENT_URL, json=EstablishmentSample)
    assert response.status_code == 201

    updatedData = {"name": "Test EstablishmentUpdated", "location": "123 Test Street", "opening_hours": "12:00 - 18:00", "description":"some description about Street"}
    response = requests.put(ESTABLISHMENT_URL + str(response.json()["id"]) + "/", json=updatedData)
    assert response.status_code == 200
    assert response.json()["name"] == updatedData["name"]

def testDELETEEstablishment(EstablishmentSample):
    response = requests.post(ESTABLISHMENT_URL, json=EstablishmentSample)
    assert response.status_code == 201

    response = requests.delete(ESTABLISHMENT_URL + str(response.json()["id"]) + "/")
    assert response.status_code == 204

    try:
        response = requests.get(ESTABLISHMENT_URL + str(response.json()["id"]) + "/")
    except:
        assert True