import pytest

from os import environ
from requests.exceptions import HTTPError

class BaseFakeStoreTest:
    ENTITY = None
    RESPONSE_DATA = []

    def mock_response(self, requests_mock, entity, json_response=None):
        url = f"{environ['FAKESTORE_URL'].rstrip('/')}/{entity}"
        if json_response is None:
            requests_mock.get(url, status_code=500)
        else:
            requests_mock.get(url, json=json_response)

    def FakeStore(self):
        from marketbridge.services.fake_store_api import FakeStoreAPI
        return FakeStoreAPI()

    def test_success(self, requests_mock):
        self.mock_response(requests_mock, self.ENTITY, self.RESPONSE_DATA)
        data = self.FakeStore().fetch(self.ENTITY)

        assert isinstance(data, list)
        assert len(data) == 2
        assert data == self.RESPONSE_DATA

    def test_invalid_format(self, requests_mock):
        self.mock_response(requests_mock, self.ENTITY, "invalid_data")

        with pytest.raises(ValueError, match="Unexpected response format"):
            self.FakeStore().fetch(self.ENTITY)

    def test_api_error(self, requests_mock):
        self.mock_response(requests_mock, self.ENTITY)

        with pytest.raises(HTTPError, match="500 Server Error"):
            self.FakeStore().fetch(self.ENTITY)