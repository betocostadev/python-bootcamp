import asyncio
from uuid import UUID

import pytest

from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductUpdate
from tests.factories import product_data_factory

# Using the event_loop fixture in the test
# This fixture is used to create a new event loop for each test function
# This is necessary because the event loop is not thread-safe


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collections_names = await mongo_client.get_database().list_collection_names()
    for collection_name in collections_names:
        print(collection_name)
        # await mongo_client.get_database()[collection_name].delete_many({})


@pytest.fixture
def product_id() -> UUID:
    return UUID("fce6cc37-10b9-4a8e-a8b2-977df327001a")


@pytest.fixture
def product_in(product_id):
    return ProductIn(**product_data_factory(), id=product_id)


@pytest.fixture
def product_up(product_id):
    return ProductUpdate(**product_data_factory(), id=product_id)
