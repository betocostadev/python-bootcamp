from typing import List
import pytest
from tests.factories import product_data_factory
from fastapi import status


async def test_controller_should_create_product(client, products_url):
    response = await client.post(products_url, json=product_data_factory())

    content = response.json()
    del content["id"]
    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_201_CREATED
    assert content == product_data_factory()


async def test_controller_should_get_product_by_id(
    client, products_url, product_inserted
):
    response = await client.get(f"{products_url}{product_inserted.id}")
    content = response.json()

    del content["created_at"]
    del content["updated_at"]

    assert response.status_code == status.HTTP_200_OK
    assert content["id"] == str(product_inserted.id)


async def test_controller_should_get_product_not_found(client, products_url):
    response = await client.get(f"{products_url}1e4f214e-85f7-461a-89d0-a751a32e3bb9")

    content = response.json()

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert content == {
        "detail": "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    }


@pytest.mark.usefixtures("products_inserted")
async def test_controller_should_query_multiple_products(
    client,
    products_url,
):
    response = await client.get(products_url)
    content = response.json()

    print(content)

    assert response.status_code == status.HTTP_200_OK
    assert isinstance(content, List)
    assert len(content) > 1


async def test_controller_should_update_product(client, products_url, product_inserted):
    response = await client.patch(
        f"{products_url}{product_inserted.id}",
        json={"quantity": 0, "status": "unavailable"},
    )

    content = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert content["quantity"] == 0
    assert content["status"] == "unavailable"
