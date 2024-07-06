from uuid import UUID

from pydantic import ValidationError
import pytest
from store.schemas.product import ProductIn
from tests.factories import product_data_factory


def test_schemas_validated():
    data = product_data_factory()
    product = ProductIn.model_validate(data)

    assert isinstance(product.id, UUID)
    assert product.name == "Samsung Galaxy S24 Ultra"
    assert product.quantity == 10
    assert product.price == 5600.0
    assert product.status == "available"


def test_schemas_return_raise():
    data = {
        "name": "Samsung Galaxy S24 Ultra",
        "quantity": 10,
        "price": 5600.0,
    }

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"name": "Samsung Galaxy S24 Ultra", "quantity": 10, "price": 5600.0},
        "url": "https://errors.pydantic.dev/2.8/v/missing",
    }
