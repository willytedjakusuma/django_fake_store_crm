import pytest
import requests
from os import environ
from requests.exceptions import HTTPError
from marketbridge.services.fake_store_api import FakeStoreAPI

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

def fetch_logic(requests_mock, entity, json_response=None):
    url = f"{environ['FAKESTORE_URL'].rstrip('/')}/{entity}"
    if json_response is None:
        requests_mock.get(url, status_code=500)
    else:
        requests_mock.get(url, json=json_response)

def fetcher():
    return FakeStoreAPI()

def test_fetch_users_success(requests_mock):
    fetch_logic(requests_mock, "users", FAKE_USER_RESPONSE)
    users = fetcher().fetch_logic("users")

    assert isinstance(users, list)
    assert len(users) == 2
    assert users[0]["username"] == "johndoe"
    assert users[1]["username"] == "janedoe"

def test_fetch_users_invalid_format(requests_mock):
    fetch_logic(requests_mock, "users", "invalid_data")

    with pytest.raises(ValueError, match="Unexpected response format"):
        fetcher().fetch_users()

def test_fetch_users_api_error(requests_mock):
    fetch_logic(requests_mock, "users")

    with pytest.raises(HTTPError, match="500 Server Error"):
        fetcher().fetch_users()