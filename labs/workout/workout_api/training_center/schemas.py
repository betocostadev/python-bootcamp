# Training Center Schema

from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class TrainingCenterSchema(BaseSchema):
    name: Annotated[
        str, Field(description="Training Center Name", example="Gavioes", max_length=30)
    ]
    address: Annotated[
        str,
        Field(
            description="Training Center Address",
            example="Rua Joca, Sao Paulo, SP",
            max_length=60,
        ),
    ]
    owner: Annotated[
        str,
        Field(
            description="Training Center Owner",
            example="Denis Quaid",
            max_length=30,
        ),
    ]
