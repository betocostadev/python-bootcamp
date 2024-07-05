# Athlete Model

from datetime import datetime
from sqlalchemy import DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship
from labs.workout.workout_api.categories.models import CategoryModel
from labs.workout.workout_api.training_center.models import TrainingCenterModel
from workout_api.contrib.models import BaseModel


class AthleteModel(BaseModel):
    __tablename__ = "athlete"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    document: Mapped[str] = mapped_column(String(14), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    weight: Mapped[float] = mapped_column(Integer, nullable=False)
    height: Mapped[float] = mapped_column(Float, nullable=False)
    sex: Mapped[str] = mapped_column(String(1), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    category: Mapped["CategoryModel"] = relationship(
        "CategoryModel", back_populates="athlete"
    )
    category_id = Mapped[int] = mapped_column(
        ForeignKey("categories.pk_id"), nullable=False
    )
    training_center: Mapped["TrainingCenterModel"] = relationship(
        "TrainingCenterModel", back_populates="athlete"
    )
    training_center_id = Mapped[int] = mapped_column(
        ForeignKey("training_centers.pk_id"), nullable=False
    )
