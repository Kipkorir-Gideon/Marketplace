from fastapi import APIRouter, HTTPException
from typing import List
from .models import Product, ProductCreate, ProductUpdate
from .utils import (
    get_product,
    create_product,
    update_product,
    delete_product,
    get_product_by_id,
)

router = APIRouter()


@router.post("/products/", response_model=Product)
async def add_product(product: ProductCreate):
    return await create_product(product)


@router.get("/products/", response_model=List[Product])
async def list_products(skip: int = 0, limit: int = 10):
    return await get_product(skip=skip, limit=limit)


@router.get("/products/{product_id}", response_model=Product)
async def get_product_details(product_id: int):
    product = await get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/products/{product_id}", response_model=Product)
async def update_product_details(product_id: int, product: ProductUpdate):
    updated_product = await update_product(product_id, product)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/products/{product_id}", response_model=dict)
async def remove_product(product_id: int):
    success = await delete_product(product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
