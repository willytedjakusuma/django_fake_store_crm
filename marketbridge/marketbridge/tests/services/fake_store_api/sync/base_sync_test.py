import pytest

from os import environ
from requests.exceptions import HTTPError
from marketbridge.services.fake_store_api.sync import sync_entity, get_entity_model
from marketbridge.services.fake_store_api.fetch import FakeStoreAPI

class BaseSyncTest:
    ENTITY = None
    ENTITY_DATA = []
    
    def test_success(self, db, monkeypatch):
        monkeypatch.setattr(FakeStoreAPI, 'fetch', lambda _self, _entity: self.ENTITY_DATA)
        sync_entity(self.ENTITY)
        
        assert get_entity_model(self.ENTITY).objects.count() == len(self.ENTITY_DATA)