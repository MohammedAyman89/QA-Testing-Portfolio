import pytest
import requests
from config import BASE_URL


@pytest.mark.regression
def test_partial_update_firstname(create_booking, auth_headers):
    payload = {"firstname": "Partial"}

    response = requests.patch(f"{BASE_URL}/booking/{create_booking}",
                              json=payload, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Partial"


@pytest.mark.regression
def test_partial_update_additional_needs(create_booking, auth_headers):
    payload = {"additionalneeds": "Late checkout"}

    response = requests.patch(f"{BASE_URL}/booking/{create_booking}",
                              json=payload, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["additionalneeds"] == "Late checkout"


@pytest.mark.regression
def test_partial_update_totalprice(create_booking, auth_headers):
    payload = {"totalprice": 500}

    response = requests.patch(f"{BASE_URL}/booking/{create_booking}",
                              json=payload, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["totalprice"] == 500
