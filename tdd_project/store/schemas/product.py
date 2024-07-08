from datetime import datetime
from typing import Optional
from pydantic import UUID4, BaseModel, Field
from store.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., json_schema_extra={"title": "Product name"})
    quantity: int = Field(..., json_schema_extra={"title": "Product quantity"})
    price: float = Field(..., json_schema_extra={"title": "Product price"})
    status: str = Field(..., json_schema_extra={"title": "Product status"})


class ProductIn(ProductBase, BaseSchemaMixin):
    pass


class ProductOut(ProductIn):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(
        ..., json_schema_extra={"title": "Product quantity"}
    )
    price: Optional[float] = Field(None, json_schema_extra={"title": "Product price"})
    status: Optional[str] = Field(None, json_schema_extra={"title": "Product status"})


class ProductUpdateOut(ProductUpdate):
    pass
