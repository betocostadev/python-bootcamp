from pydantic import Field
from store.schemas.base import BaseSchemaMixin


class ProductIn(BaseSchemaMixin):
    name: str = Field(..., json_schema_extra={"title": "Product name"})
    quantity: int = Field(..., json_schema_extra={"title": "Product quantity"})
    price: float = Field(..., json_schema_extra={"title": "Product price"})
    status: str = Field(..., json_schema_extra={"title": "Product status"})
