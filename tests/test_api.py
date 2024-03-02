import pytest
import requests

ESTABLISHMENT_URL = "http://0.0.0.0:8000/api/v1/establishments/"
PRODUCT_URL = "http://0.0.0.0:8000/api/v1/products/"

@pytest.fixture
def EstablishmentSample():
    return {"name": "Test Establishment", "address": "123 Test St", "category": "Test"}


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

    updatedData = {"name": "Test EstablishmentUpdated", "address": "123 Test St", "category": "Test"}
    response = requests.put(ESTABLISHMENT_URL + str(response.json()["id"]) + "/", json=updatedData)
    assert response.status_code == 200
    assert response.json()["name"] == updatedData["name"]

def testDELETEEstablishment(EstablishmentSample):
    response = requests.post(ESTABLISHMENT_URL, json=EstablishmentSample)
    assert response.status_code == 201

    response = requests.delete(ESTABLISHMENT_URL + str(response.json()["id"]) + "/")
    assert response.status_code == 204

    response = requests.get(ESTABLISHMENT_URL + str(response.json()["id"]) + "/")
    assert response.status_code == 404
