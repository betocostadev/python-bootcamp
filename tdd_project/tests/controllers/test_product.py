from tests.factories import product_data_factory
from fastapi import status


async def test_controllers_should_create_product(client, products_url):
    response = await client.post(products_url, json=product_data_factory())

    assert response.status_code == status.HTTP_201_CREATED
    # assert response.json() == product_data_factory()


# async def test_controller_should_get_products
