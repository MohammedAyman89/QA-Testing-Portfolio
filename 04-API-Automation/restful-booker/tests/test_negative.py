import pytest
import requests
from config import BASE_URL, AUTH_CREDENTIALS, BOOKING_PAYLOAD


@pytest.mark.negative
def test_get_booking_invalid_id():
    response = requests.get(f"{BASE_URL}/booking/999999")
    assert response.status_code == 404


@pytest.mark.negative
@pytest.mark.parametrize("missing_field", [
    "firstname",
    "lastname",
    "totalprice",
    "bookingdates",
], ids=[
    "missing_firstname",
    "missing_lastname",
    "missing_totalprice",
    "missing_bookingdates",
])
def test_create_booking_missing_field(missing_field):
    payload = BOOKING_PAYLOAD.copy()
    del payload[missing_field]

    response = requests.post(f"{BASE_URL}/booking", json=payload)
    assert response.status_code == 400, f"BUG: API returns 500 instead of 400 when {missing_field} is missing"


@pytest.mark.negative
@pytest.mark.parametrize("method", [
    "PUT",
    "PATCH",
    "DELETE",
], ids=[
    "update_no_auth",
    "partial_update_no_auth",
    "delete_no_auth",
])
def test_protected_endpoints_without_auth(create_booking, method):
    url = f"{BASE_URL}/booking/{create_booking}"
    response = requests.request(method, url, json={"firstname": "Hacker"})
    assert response.status_code == 403


@pytest.mark.negative
def test_update_nonexistent_booking(auth_headers):
    updated_payload = BOOKING_PAYLOAD.copy()

    response = requests.put(f"{BASE_URL}/booking/999999",
                            json=updated_payload, headers=auth_headers)
    assert response.status_code == 404, "BUG: API returns 405 instead of 404 for non-existent booking update"


@pytest.mark.negative
def test_delete_nonexistent_booking(auth_headers):
    response = requests.delete(f"{BASE_URL}/booking/999999",
                               headers=auth_headers)
    assert response.status_code == 404, "BUG: API returns 405 instead of 404 for non-existent booking delete"


@pytest.mark.negative
@pytest.mark.parametrize("username,password", [
    ("admin", "wrong"),
    ("hacker", "password123"),
], ids=[
    "wrong_password",
    "wrong_username",
])
def test_auth_invalid_credentials(username, password):
    response = requests.post(f"{BASE_URL}/auth",
                             json={"username": username, "password": password})
    assert response.status_code == 401, "BUG: API returns 200 instead of 401 for invalid credentials"
    assert "Bad credentials" in response.json().get("reason", "")
