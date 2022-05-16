import pytest
from fastapi.testclient import TestClient

from app.main import app

def test_save_staticss():
    request_data1 = {
        "date": "2020-05-15",
        "views": 100,
        "clicks": 50,
        "cost": 25
    }
    request_data2 = {
        "date": "2022-03-15",
        "views": 150,
        "clicks": 25,
        "cost": 50.55
    }
    request_data3 = {
        "date": "2022-05-15",
        "views": 50,
        "clicks": 60,
        "cost": 34.65
    }

    with TestClient(app) as client:
        response1 = client.post("/save-statics", json=request_data1)
        response2 = client.post("/save-statics", json=request_data2)
        response3 = client.post("/save-statics", json=request_data3)
    assert response1.status_code == 200
    assert response2.status_code == 200
    assert response3.status_code == 200

def test_read_statics():
    with TestClient(app) as client:
        response = client.get("/read-staticks?from_date=2020-07-16&to_date=2022-05-15&name_column_sorted=cpc&sorting_from_last=true")
    assert response.status_code == 200
    assert response.json()[0]["date"] == "2022-05-15"
    assert response.json()[0]["views"] == 50
    assert response.json()[0]["clicks"] == 60
    assert response.json()[0]["cost"] == 34.65
    assert response.json()[0]["cpc"] == 0.5775
    assert response.json()[0]["cpm"] == 577.5




def test_reset_statics():
    with TestClient(app) as client:
        response = client.delete("/reset-statics")
    assert response.status_code == 200