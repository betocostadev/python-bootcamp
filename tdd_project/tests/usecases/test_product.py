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


# async def test_usecases_should_get_product_by_id(product_id):
#     result = await product_usecase.get(id=product_id)
# Updated to use the product_inserted fixture.
# This fixture creates a product and returns the product object.
async def test_usecases_should_get_product_by_id(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, ProductOut)
    assert result.name == "Samsung Galaxy S24 Ultra"


async def test_usecases_get_wrong_id_should_return_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )


# Changed the test to use products_inserted fixture
# It will add multiple products to the database and query them.
@pytest.mark.usefixtures("products_inserted")
async def test_usecases_should_query_multiple_products():
    # result = await product_usecase.query(status="available")
    result = await product_usecase.query()

    assert isinstance(result, List)
    assert len(result) > 1


# async def test_usecases_should_update_product_by_id(product_id, product_up):
async def test_usecases_should_update_product_by_id(product_inserted, product_up):
    product_up.price = "5900.49"
    result = await product_usecase.update(id=product_inserted.id, body=product_up)

    assert isinstance(result, ProductUpdateOut)


# async def test_usecases_should_delete_product_by_id(product_id):
async def test_usecases_should_delete_product_by_id(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecases_delete_wrong_id_should_return_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )
