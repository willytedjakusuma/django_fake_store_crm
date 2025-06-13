import requests
from requests.exceptions import HTTPError

class FakeStore:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')

    def fetch_logic(self, entity: str):
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

    def fetch_users(self):
        return self.fetch_logic("users")