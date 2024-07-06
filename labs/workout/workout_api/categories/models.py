# Category Model

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.atlhete.models import AthleteModel
from workout_api.contrib.models import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = "categories"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    atlhetes: Mapped["AthleteModel"] = relationship(
        "AthleteModel", back_populates="categories"
    )
