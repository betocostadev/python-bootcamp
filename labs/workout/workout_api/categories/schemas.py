# Category Schema

from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CategorySchema(BaseSchema):
    name: Annotated[
        str, Field(description="Category name", example="Cardio", max_length=50)
    ]
