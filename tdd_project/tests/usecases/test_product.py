from store.usecases.product import product_usecase


async def test_usecases_should_return_success():
    result = await product_usecase.create()
    print(result)
    pass

    # assert isinstance(result, ProductOut)
