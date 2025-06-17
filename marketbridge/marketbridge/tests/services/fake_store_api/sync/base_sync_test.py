import pytest

from os import environ
from requests.exceptions import HTTPError
from marketbridge.services.fake_store_api.sync import sync_entities
from marketbridge.services.fake_store_api.fetch import FakeStoreAPI

class BaseSyncTest:
    ENTITY = None
    ENTITY_NAME = None
    ENTITY_DATA = []
    
    def test_success(self, db, monkeypatch):
        monkeypatch.setattr(FakeStoreAPI, 'fetch', lambda self, entity: self.ENTITY_DATA)
        sync_entities(self.ENTITY_NAME)
        
        assert self.ENTITY.objects.count() == len(self.ENTITY_DATA)