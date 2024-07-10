from decimal import Decimal
from typing import Annotated, Optional
from bson import Decimal128
from pydantic import AfterValidator, BaseModel, Field
from store.schemas.base import BaseSchemaMixin, OutMixin


# Changed base model price to use Decimal
# Since MongoDB does not have a Decimal type, we will convert it.
class ProductBase(BaseModel):
    name: str = Field(..., json_schema_extra={"title": "Product name"})
    quantity: int = Field(..., json_schema_extra={"title": "Product quantity"})
    price: Decimal = Field(..., json_schema_extra={"title": "Product price"})
    status: str = Field(..., json_schema_extra={"title": "Product status"})


class ProductIn(ProductBase, BaseSchemaMixin):
    pass


class ProductOut(ProductIn, OutMixin):
    pass


# Added Decimal_ to convert Decimal to Decimal128
# Making it compatible with MongoDB
def convert_decimal_128(value: Decimal):
    return Decimal128(str(value))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class ProductUpdate(ProductBase):
    quantity: Optional[int] = Field(
        ..., json_schema_extra={"title": "Product quantity"}
    )
    price: Optional[Decimal_] = Field(
        None, json_schema_extra={"title": "Product price"}
    )
    status: Optional[str] = Field(None, json_schema_extra={"title": "Product status"})


class ProductUpdateOut(ProductUpdate, OutMixin):
    pass
