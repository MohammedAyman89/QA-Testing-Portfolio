import requests
from config import BASE_URL


def test_get_all_bookings():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "bookingid" in response.json()[0]

def test_get_single_booking(create_booking):
    response = requests.get(f"{BASE_URL}/booking/{create_booking}")
    assert response.status_code == 200
    assert "firstname" in response.json()
    assert "lastname" in response.json()