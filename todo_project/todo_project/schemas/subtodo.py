# todo_project/schemas/subtodo.py

from pydantic import Field

from todo_project.schemas.base import BaseSchemaMixin, OutSchema


class SubTodoSchema(OutSchema, BaseSchemaMixin):
    title: str = Field(max_length=256)
