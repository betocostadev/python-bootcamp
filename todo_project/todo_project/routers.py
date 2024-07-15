# todo_project/routers.py

from fastapi import APIRouter

from todo_project.controllers.todo import router as todo_router

api_router = APIRouter()
api_router.include_router(todo_router)
