import logging
from .fetch import FakeStoreAPI
from django.apps import apps


logger = logging.getLogger(__name__)

AVAILABLE_ENTITIES = {
        "users": ("accounts", "User"),
    }
    

def sync_entity(entity_name: str):
    data = fetch_from_api(entity_name)
    try:
        entity_model = get_entity_model(entity_name)
        records = populate_data_into_model(entity_model, data)
        entity_model.objects.bulk_create(
            records,
            update_conflicts=True,
            unique_fields=['id'],  # Assuming 'id' is the unique field for the entity
            update_fields=[f.name for f in entity_model._meta.fields if f.name != 'id']
        )
        
    except Exception as e:
        logger.error(f"Failed to store data for {entity_name}: {e}")
        raise
    
def populate_data_into_model(entity_model, data):
    return [entity_model(**item) for item in data]
    
    
def fetch_from_api(entity_name: str):
    try:
        data = FakeStoreAPI().fetch(entity_name)
        
        return data
        
    except Exception as e:
        logger.error(f"Failed to fetch data for {entity_name}: {e}")
        raise

def get_entity_model(entity_name: str):
    if entity_name not in AVAILABLE_ENTITIES:
        raise ValueError(f"Unknown entity: {entity_name}")
    
    app_label, model_name = AVAILABLE_ENTITIES[entity_name]
    
    return apps.get_model(app_label, model_name)