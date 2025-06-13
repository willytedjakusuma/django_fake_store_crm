from marketbridge.tests.services.fake_store_api.test_base import BaseFakeStoreTest

class TestFetchProducts(BaseFakeStoreTest):
    ENTITY = "products"
    RESPONSE_DATA = [
        {"id": 1, "title": "Product A", "price": 19.99},
        {"id": 2, "title": "Product B", "price": 29.99},
    ]
