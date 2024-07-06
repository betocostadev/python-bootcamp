from motor.motor_asyncio import AsyncIOMotorClient

from store.core.config import settings


class MongoClient:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)
        self.db = self.client["dio-tdd-project"]

    def get(self) -> AsyncIOMotorClient:
        return self.client

    # def connect(self):
    #     return f"Connected to {self.host}:{self.port}"


db_client = MongoClient()
# print(db_client)
