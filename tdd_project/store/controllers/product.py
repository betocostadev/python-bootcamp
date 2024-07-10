from fastapi import APIRouter, Body, Depends, status
from store.schemas.product import ProductIn, ProductOut
from store.usecases.product import ProductUsecase


router = APIRouter(tags=["products"])


@router.post(path="/products/", status_code=status.HTTP_201_CREATED)
async def create_product(
    body: ProductIn = Body(...), usecase: ProductUsecase = Depends()
) -> ProductOut:
    return await usecase.create(body=body)


@router.get("/products/", tags=["products"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]
