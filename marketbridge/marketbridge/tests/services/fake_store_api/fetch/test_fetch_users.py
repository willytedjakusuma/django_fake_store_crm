from marketbridge.tests.services.fake_store_api.fetch.base_fetch_test import BaseFetchTest

class TestFetchUsers(BaseFetchTest):
    ENTITY = "users"
    RESPONSE_DATA = [
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
