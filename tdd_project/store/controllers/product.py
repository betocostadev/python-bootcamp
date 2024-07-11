from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Path, status
from pydantic import UUID4
from store.core.exceptions import NotFoundException
from store.schemas.product import ProductIn, ProductOut, ProductUpdate, ProductUpdateOut
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


@router.get(
    "/products/", response_model=List[ProductOut], status_code=status.HTTP_200_OK
)
async def query_products(usecase: ProductUsecase = Depends()) -> List[ProductOut]:
    return await usecase.query()


@router.patch(
    "/products/{id}", response_model=ProductOut, status_code=status.HTTP_200_OK
)
async def update_product(
    id: UUID4 = Path(alias="id"),
    body: ProductUpdate = Body(...),
    usecase: ProductUsecase = Depends(),
) -> ProductUpdateOut:
    try:
        return await usecase.update(id=id, body=body)
    except NotFoundException as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.message)


@router.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    id: UUID4 = Path(alias="id"), usecase: ProductUsecase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as err:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=err.message)
