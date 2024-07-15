# todo_project/controllers/todo.py

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.param_functions import Query
from datetime import date
from typing import Optional

from todo_project.schemas.todo import TodoSchema, SubTodoSchema
from todo_project.models.todo import TodoModel
from todo_project.usecases.todo import TodoUseCases


router = APIRouter(prefix="/todos", tags=["todos"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TodoSchema)
async def create_todo(todo: TodoSchema, usecases: TodoUseCases = Depends()):
    todo_model = TodoModel(**todo.dict())
    new_todo = await usecases.create_todo(todo_model)
    return new_todo


@router.get("/", status_code=status.HTTP_200_OK, response_model=list[TodoSchema])
async def get_all_todos(
    usecases: TodoUseCases = Depends(),
    completed: Optional[bool] = Query(None, alias="completed"),
    title: Optional[str] = Query(None, alias="title"),
    is_flagged: Optional[bool] = Query(None, alias="is_flagged"),
    due_date: Optional[date] = Query(None, alias="due_date"),
):
    if completed is not None:
        todos = await usecases.get_todos_by_status(completed)
    elif title is not None:
        todos = await usecases.get_todos_by_title(title)
    elif is_flagged is not None:
        todos = await usecases.get_todos_by_is_flagged(is_flagged)
    elif due_date is not None:
        todos = await usecases.get_todos_by_due_date(due_date)
    else:
        todos = await usecases.get_all_todos()
    return todos


@router.get("/{todo_id}", status_code=status.HTTP_200_OK, response_model=TodoSchema)
async def get_todo(todo_id: str, usecases: TodoUseCases = Depends()):
    todo = await usecases.get_todo(todo_id)
    if todo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Tarefa não encontrada"
        )
    return todo


@router.put("/{todo_id}", status_code=status.HTTP_200_OK, response_model=TodoSchema)
async def update_todo(
    todo_id: str, todo: TodoSchema, usecases: TodoUseCases = Depends()
):
    updated_todo = await usecases.update_todo(todo_id, todo)
    return updated_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(todo_id: str, usecases: TodoUseCases = Depends()):
    await usecases.delete_todo(todo_id)
    return JSONResponse(
        status_code=status.HTTP_204_NO_CONTENT, content="Tarefa deletada"
    )


@router.post(
    "/{todo_id}/sub-tasks",
    status_code=status.HTTP_201_CREATED,
    response_model=SubTodoSchema,
)
async def create_sub_task(
    todo_id: str, sub_task: SubTodoSchema, usecases: TodoUseCases = Depends()
):
    new_sub_task = await usecases.create_sub_task(todo_id, sub_task)
    return new_sub_task
