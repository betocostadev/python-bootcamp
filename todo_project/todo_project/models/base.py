# todo_project/models/base.py

from typing import Optional

from pydantic import BaseModel, Field

from todo_project.schemas.base import OutSchema


class BaseSchemaMixin(BaseModel):
    class Config:
        from_attributes = True


class MongoModel(OutSchema, BaseSchemaMixin):
    id: Optional[str] = Field(alias="_id")
