# todo_project/schemas/todo.py

from datetime import time, date
from typing import Optional
from pydantic import Field

from todo_project.schemas.base import BaseSchemaMixin
from todo_project.schemas.subtodo import SubTodoSchema


class TodoSchema(BaseSchemaMixin):
    title: str = Field(max_length=256)
    note: Optional[str] = Field(max_length=1024, default="")
    url: Optional[str] = Field(max_length=256, default="")
    due_date: Optional[date] = Field(None, alias="date")
    due_time: Optional[time] = Field(None, alias="time")
    priority: str = Field(default="none", max_length=5, pattern=r"none|low|mid|high")
    is_flagged: bool = Field(default=False)
    sub_tasks: list[SubTodoSchema] = Field(default_factory=list)
