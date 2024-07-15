# todo_project/main.py

from fastapi import FastAPI

from todo_project.routers import api_router

app = FastAPI(title="Todo Project", version="0.1.0")
app.include_router(api_router)
