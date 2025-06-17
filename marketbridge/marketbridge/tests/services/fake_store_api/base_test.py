import pytest

from os import environ
from requests.exceptions import HTTPError

class BaseFakeStoreTest:
    ENTITY = None
    RESPONSE_DATA = []

    def mock_response(self, requests_mock, entity, json_response=None, raise_exc=None):
        url = f"{environ['FAKESTORE_URL'].rstrip('/')}/{entity}"
        if raise_exc:
            requests_mock.get(url, exc=raise_exc)
        elif json_response is None:
            requests_mock.get(url, status_code=500)
        else:
            requests_mock.get(url, json=json_response)

    def FakeStore(self):
        from marketbridge.services.fake_store_api.fetch import FakeStoreAPI
        return FakeStoreAPI()

    def test_success(self, requests_mock):
        self.mock_response(requests_mock, self.ENTITY, self.RESPONSE_DATA)
        data = self.FakeStore().fetch(self.ENTITY)

        assert isinstance(data, list)
        assert len(data) == 2
        assert data == self.RESPONSE_DATA
        
        for item in data:
            match self.ENTITY:
                case "products":
                    assert "id" in item
                    assert isinstance(item["id"], int)
                    assert "title" in item
                    assert isinstance(item["title"], str)
                    assert "price" in item
                    assert isinstance(item["price"], (float, int))
                    assert "description" in item
                    assert isinstance(item["description"], str)
                    assert "category" in item
                    assert isinstance(item["category"], str)
                    assert "image" in item
                    assert isinstance(item["image"], str)
                case "users":
                    assert "id" in item
                    assert isinstance(item["id"], int)
                    assert "username" in item
                    assert isinstance(item["username"], str)
                    assert "email" in item
                    assert isinstance(item["email"], str)
                    assert "password" in item
                    assert isinstance(item["password"], str)

    def test_invalid_format(self, requests_mock):
        self.mock_response(requests_mock, self.ENTITY, "invalid_data")

        with pytest.raises(ValueError, match="Unexpected response format"):
            self.FakeStore().fetch(self.ENTITY)

    def test_api_error(self, requests_mock):
        self.mock_response(requests_mock, self.ENTITY)

        with pytest.raises(HTTPError, match="500 Server Error"):
            self.FakeStore().fetch(self.ENTITY)
            
    def test_network_error(self, requests_mock):
        self.mock_response(requests_mock, self.ENTITY, raise_exc=ConnectionError("Network error"))
        
        with pytest.raises(ConnectionError, match="Network error"):
            self.FakeStore().fetch(self.ENTITY) 