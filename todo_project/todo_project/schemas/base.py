# todo_project/schemas/base.py

from datetime import datetime
from pydantic import UUID4, BaseModel, Field


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True


class OutSchema(BaseModel):
    id: UUID4 = Field()
    completed: bool = Field(default=False)
    created_at: datetime = Field()
    updated_at: datetime = Field()
