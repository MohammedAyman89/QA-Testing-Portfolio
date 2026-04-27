import requests
from config import BASE_URL

def test_health_check():
    response = requests.get(f"{BASE_URL}/ping")
    assert response.status_code == 201