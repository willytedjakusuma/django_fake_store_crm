from marketbridge.tests.services.fake_store_api.base_test import BaseFakeStoreTest

class TestFetchProducts(BaseFakeStoreTest):
    ENTITY = "products"
    RESPONSE_DATA = [
        {"id": 1, "title": "Product A", "price": 19.99, "description": "Description of Product A", "category": "Category A", "image": "http://example.com/imageA.jpg"},
        {"id": 2, "title": "Product B", "price": 29.99, "description": "Description of Product B", "category": "Category B", "image": "http://example.com/imageB.jpg"},
    ]
