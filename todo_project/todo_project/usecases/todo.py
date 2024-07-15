# todo_project/usecases/todo.py

from typing import List
from datetime import date

from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from todo_project.models.todo import TodoModel
from todo_project.schemas.todo import TodoSchema
from todo_project.db.mongo import db_client


class TodoUseCases:
    def __init__(self, db: AsyncIOMotorClient = Depends(db_client.get)) -> None:
        self.db = db.db["todos"]

    async def create_todo(self, todo: TodoModel) -> TodoSchema:
        result = await self.db.insert_one(todo.model_dump())
        new_todo = await self.db.find_one({"_id": result.inserted_id})
        return TodoSchema(**new_todo)

    async def get_all_todos(self) -> List[TodoSchema]:
        todos = await self.db.find().to_list(length=None)
        return [TodoSchema(**todo) for todo in todos]

    async def get_todo(self, todo_id: str) -> TodoSchema:
        todo = await self.db.find_one({"_id": todo_id})
        return TodoSchema(**todo)

    async def update_todo(self, todo_id: str, todo: TodoSchema) -> TodoSchema:
        await self.db.update_one(
            {"_id": todo_id}, {"$set": todo.model_dump(exclude={"id"})}
        )
        updated_todo = await self.db.find_one({"_id": todo_id})
        return TodoSchema(**updated_todo)

    async def delete_todo(self, todo_id: str) -> None:
        await self.db.delete_one({"_id": todo_id})

    async def get_todos_by_status(self, completed: bool) -> List[TodoSchema]:
        todos = await self.db.find({"completed": completed}).to_list(length=None)
        return [TodoSchema(**todo) for todo in todos]

    async def get_todos_by_title(self, title: str) -> List[TodoSchema]:
        todos = await self.db.find(
            {"title": {"$regex": title, "$options": "i"}}
        ).to_list(length=None)
        return [TodoSchema(**todo) for todo in todos]

    async def get_todos_by_is_flagged(self, is_flagged: bool) -> List[TodoSchema]:
        todos = await self.db.find({"is_flagged": is_flagged}).to_list(length=None)
        return [TodoSchema(**todo) for todo in todos]

    async def get_todos_by_due_date(self, due_date: date) -> List[TodoSchema]:
        todos = await self.db.find({"due_date": due_date}).to_list(length=None)
        return [TodoSchema(**todo) for todo in todos]
