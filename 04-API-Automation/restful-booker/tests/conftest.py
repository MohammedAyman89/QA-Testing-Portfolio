import os
import pytest
import requests
from config import AUTH_CREDENTIALS, BASE_URL, BOOKING_PAYLOAD


@pytest.fixture
def auth_token():
    response = requests.post(f"{BASE_URL}/auth", json=AUTH_CREDENTIALS)
    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture
def auth_headers(auth_token):
    return {"Cookie": f"token={auth_token}"}


@pytest.fixture
def create_booking():
    response = requests.post(f"{BASE_URL}/booking", json=BOOKING_PAYLOAD)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]
    yield booking_id
    token = requests.post(f"{BASE_URL}/auth", json=AUTH_CREDENTIALS).json()["token"]
    requests.delete(f"{BASE_URL}/booking/{booking_id}",
                    headers={"Cookie": f"token={token}"})


def pytest_runtest_makereport(item, call):
    if call.when == "call" and call.excinfo:
        log_dir = "failure_logs"
        os.makedirs(log_dir, exist_ok=True)

        log_file = f"{log_dir}/{item.name}.txt"
        with open(log_file, "w") as f:
            f.write(f"Test: {item.name}\n")
            f.write(f"Error: {call.excinfo.value}\n")
            for name, val in item.funcargs.items():
                f.write(f"\n{name}: {val}\n")
