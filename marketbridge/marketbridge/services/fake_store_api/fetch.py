import requests
import os
from requests.exceptions import HTTPError

class FakeStoreAPI:
    def __init__(self):
        self.base_url = os.environ['FAKESTORE_URL'].rstrip('/')

    def fetch(self, entity: str):
        url = f"{self.base_url}/{entity}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
        except HTTPError as http_err:
            raise http_err
        except requests.RequestException as req_err:
            raise ValueError(f"Request failed, error: {req_err}") from req_err

        try:
            data = response.json()
        except ValueError:
            raise ValueError(f"Failed to parse JSON response")
        
        if not isinstance(data, list):
            raise ValueError(f"Unexpected response format")

        return data