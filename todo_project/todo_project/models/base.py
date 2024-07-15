# todo_project/models/base.py

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True


class MongoModel(BaseModel):
    id: Optional[str] = Field(alias="_id")
    completed: bool = Field(default=False)
    created_at: datetime = Field()
    updated_at: datetime = Field()
