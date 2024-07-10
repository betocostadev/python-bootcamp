from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from pydantic import UUID4
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductIn, ProductOut
from store.usecases.product import ProductUsecase


router = APIRouter(tags=["products"])


@router.post(path="/products/", status_code=status.HTTP_201_CREATED)
async def create_product(
    body: ProductIn = Body(...), usecase: ProductUsecase = Depends()
) -> ProductOut:
    return await usecase.create(body=body)


@router.get("/products/{id}", response_model=ProductOut, status_code=status.HTTP_200_OK)
async def get_product(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> ProductOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.message)
