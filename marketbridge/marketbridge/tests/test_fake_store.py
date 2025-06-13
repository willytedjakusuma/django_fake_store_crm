import pytest
import requests
from requests.exceptions import HTTPError
from marketbridge.services.fake_store import FakeStore

FAKE_USER_RESPONSE = [
    {
        "id": 1,
        "username": "johndoe",
        "email": "johndoe@example.com",
        "password": "hashed_password",
    },
    {
        "id": 2,
        "username": "janedoe",
        "email": "janedoe@example.com",
        "password": "hashed_password",
    },
]

@pytest.fixture
def fake_store_url():
    return "https://fakestoreapi.com"

def fetch_logic(requests_mock, url, entity, json_response=None):
    url = f"{url}/{entity}"
    if json_response is None:
        requests_mock.get(url, status_code=500)
    else:
        requests_mock.get(url, json=json_response)

def fetcher(url):
    return FakeStore(base_url=url)

def test_fetch_users_success(requests_mock, fake_store_url):
    fetch_logic(requests_mock, fake_store_url, "users", FAKE_USER_RESPONSE)
    users = fetcher(fake_store_url).fetch_logic("users")

    assert isinstance(users, list)
    assert len(users) == 2
    assert users[0]["username"] == "johndoe"
    assert users[1]["username"] == "janedoe"

def test_fetch_users_invalid_format(requests_mock, fake_store_url):
    fetch_logic(requests_mock, fake_store_url, "users", "invalid_data")

    with pytest.raises(ValueError, match="Unexpected response format"):
        fetcher(fake_store_url).fetch_users()

def test_fetch_users_api_error(requests_mock, fake_store_url):
    fetch_logic(requests_mock, fake_store_url, "users")

    with pytest.raises(HTTPError, match="500 Server Error"):
        fetcher(fake_store_url).fetch_users()