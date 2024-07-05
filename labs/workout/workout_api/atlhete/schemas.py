# Athlete Schema

from typing import Annotated
from pydantic import Field, PositiveFloat
from workout_api.contrib.schemas import BaseSchema


class AthleteSchema(BaseSchema):
    name: Annotated[
        str, Field(description="Athlete name", example="John Doe", max_length=50)
    ]
    document: Annotated[
        str,
        Field(description="Athlete Document", example="12345678900", max_length=14),
    ]
    age: Annotated[int, Field(description="Athlete age", example=30)]
    weight: Annotated[PositiveFloat, Field(description="Athlete Weight", example=97.5)]
    height: Annotated[PositiveFloat, Field(description="Athlete Height", example=1.85)]
    sex: Annotated[str, Field(description="Athlete Sex", example="M", max_length=1)]
