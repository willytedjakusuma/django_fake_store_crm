from marketbridge.tests.services.fake_store_api.sync.base_sync_test import BaseSyncTest

class TestSyncUsers(BaseSyncTest):
    ENTITY = "users"
    ENTITY_DATA = [
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
            "password": "secret_hashed_password",
        },
    ]