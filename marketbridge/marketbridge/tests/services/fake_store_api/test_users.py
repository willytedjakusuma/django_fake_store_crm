from marketbridge.tests.services.fake_store_api.base_test import BaseFakeStoreTest

class TestFetchUsers(BaseFakeStoreTest):
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
