# Training Center Model

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from workout_api.atlhete.models import AthleteModel
from workout_api.contrib.models import BaseModel


class TrainingCenterModel(BaseModel):
    __tablename__ = "training_centers"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    address: Mapped[str] = mapped_column(String(60), nullable=False)
    owner: Mapped[str] = mapped_column(String(30), nullable=False)
    atlhetes: Mapped["AthleteModel"] = relationship(
        "AthleteModel", back_populates="training_centers"
    )
