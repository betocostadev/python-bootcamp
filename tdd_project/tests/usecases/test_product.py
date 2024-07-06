from typing import List
from uuid import UUID
import pytest
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase


async def test_usecases_should_create_product(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == product_in.name


async def test_usecases_should_get_product_by_id(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Samsung Galaxy S24 Ultra"


async def test_usecases_should_get_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )


async def test_usercases_should_query_multiple_products():
    # result = await product_usecase.query(status="active")

    result = await product_usecase.query()
    assert isinstance(result, List)
    assert len(result) > 1


async def test_usercases_should_update_product_by_id(product_id, product_up):
    product_up.price = 5900.49
    result = await product_usecase.update(id=product_id, body=product_up)

    assert isinstance(result, ProductUpdateOut)
