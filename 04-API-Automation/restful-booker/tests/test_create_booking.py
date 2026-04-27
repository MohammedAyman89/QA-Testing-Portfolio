import pytest
import requests
from config import BASE_URL, BOOKING_PAYLOAD


@pytest.mark.smoke
def test_create_booking():
    response = requests.post(f"{BASE_URL}/booking", json=BOOKING_PAYLOAD)
    assert response.status_code == 200

    body = response.json()
    assert "bookingid" in body
    assert body["booking"]["firstname"] == BOOKING_PAYLOAD["firstname"]
    assert body["booking"]["lastname"] == BOOKING_PAYLOAD["lastname"]
    assert body["booking"]["totalprice"] == BOOKING_PAYLOAD["totalprice"]
    assert body["booking"]["depositpaid"] == BOOKING_PAYLOAD["depositpaid"]
    assert body["booking"]["additionalneeds"] == BOOKING_PAYLOAD["additionalneeds"]


@pytest.mark.regression
def test_create_booking_without_additional_needs():
    payload = BOOKING_PAYLOAD.copy()
    del payload["additionalneeds"]

    response = requests.post(f"{BASE_URL}/booking", json=payload)
    assert response.status_code == 200
    assert "bookingid" in response.json()


@pytest.mark.regression
def test_create_booking_dates_match():
    response = requests.post(f"{BASE_URL}/booking", json=BOOKING_PAYLOAD)
    assert response.status_code == 200

    booking = response.json()["booking"]
    assert booking["bookingdates"]["checkin"] == BOOKING_PAYLOAD["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == BOOKING_PAYLOAD["bookingdates"]["checkout"]
