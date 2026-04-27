import pytest
import requests
from config import BASE_URL, BOOKING_PAYLOAD


@pytest.mark.regression
def test_update_booking(create_booking, auth_headers):
    updated_payload = BOOKING_PAYLOAD.copy()
    updated_payload["firstname"] = "Updated"
    updated_payload["lastname"] = "Name"
    updated_payload["totalprice"] = 200

    response = requests.put(f"{BASE_URL}/booking/{create_booking}",
                            json=updated_payload, headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["firstname"] == "Updated"
    assert response.json()["lastname"] == "Name"
    assert response.json()["totalprice"] == 200


@pytest.mark.regression
def test_update_booking_returns_all_fields(create_booking, auth_headers):
    updated_payload = BOOKING_PAYLOAD.copy()
    updated_payload["firstname"] = "James"

    response = requests.put(f"{BASE_URL}/booking/{create_booking}",
                            json=updated_payload, headers=auth_headers)
    assert response.status_code == 200

    body = response.json()
    assert "firstname" in body
    assert "lastname" in body
    assert "totalprice" in body
    assert "depositpaid" in body
    assert "bookingdates" in body
    assert "additionalneeds" in body
