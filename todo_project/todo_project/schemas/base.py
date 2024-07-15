# todo_project/schemas/base.py

from datetime import datetime
from pydantic import BaseModel, Field


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True


class OutSchema(BaseModel):
    id: str = Field(alias="_id")
    completed: bool = Field(default=False)
    created_at: datetime = Field()
    updated_at: datetime = Field()
