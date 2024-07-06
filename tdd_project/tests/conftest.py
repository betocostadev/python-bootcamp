import asyncio

import pytest

from store.db.mongo import db_client

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
        await mongo_client.get_database()[collection_name].delete_many({})
