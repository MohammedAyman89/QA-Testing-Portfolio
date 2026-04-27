import pytest
import requests
from config import BASE_URL


@pytest.mark.smoke
def test_delete_booking(create_booking, auth_headers):
    response = requests.delete(f"{BASE_URL}/booking/{create_booking}",
                               headers=auth_headers)
    assert response.status_code == 201


@pytest.mark.regression
def test_deleted_booking_returns_404(create_booking, auth_headers):
    requests.delete(f"{BASE_URL}/booking/{create_booking}", headers=auth_headers)

    response = requests.get(f"{BASE_URL}/booking/{create_booking}")
    assert response.status_code == 404
