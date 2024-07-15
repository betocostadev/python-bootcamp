# todo_project/schemas/todo.py

from datetime import time, date
from pydantic import Field

from todo_project.schemas.base import BaseSchemaMixin, OutSchema
from todo_project.schemas.subtodo import SubTodoSchema


class TodoSchema(OutSchema, BaseSchemaMixin):
    title: str = Field(max_length=256)
    note: str = Field(max_length=1024, default="")
    url: str = Field(max_length=256, default="")
    due_date: date = Field()
    due_time: time = Field(..., alias="time")
    priority: str = Field(default="none", max_length=5, regex=r"none|low|mid|high")
    is_flagged: bool = Field(default=False)
    sub_tasks: list[SubTodoSchema] = Field(default_factory=list)
