from typing import Optional
from pydantic import BaseModel, Field
from store.schemas.base import BaseSchemaMixin


class ProductBase(BaseModel):
    name: str = Field(..., json_schema_extra={"title": "Product name"})
    quantity: int = Field(..., json_schema_extra={"title": "Product quantity"})
    price: float = Field(..., json_schema_extra={"title": "Product price"})
    status: str = Field(..., json_schema_extra={"title": "Product status"})


class ProductIn(ProductBase, BaseSchemaMixin):
    pass


class ProductOut(ProductIn):
    pass


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(
        ..., json_schema_extra={"title": "Product quantity"}
    )
    price: Optional[float] = Field(None, json_schema_extra={"title": "Product price"})
    status: Optional[str] = Field(None, json_schema_extra={"title": "Product status"})


class ProductUpdateOut(ProductUpdate):
    pass
