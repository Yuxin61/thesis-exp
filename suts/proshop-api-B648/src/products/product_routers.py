from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import product_crud as crud
from .product_schemas import Product, ProductCreate
from ..database import get_db

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Product not found"}},
)


@router.get("/", response_model=List[Product], summary="Get all products")
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@router.get("/id/{product_id}", response_model=Product, summary="Get product by id")
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


@router.post("/", response_model=Product, summary="Create product")
def create_product(product: ProductCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product, user_id=user_id)


@router.put("/id/{product_id}", response_model=Product, summary="Update product")
def update_product(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db=db, product=product, product_id=product_id)


@router.delete("/id/{product_id}", response_model=Product, summary="Delete product")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product_by_id(db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.delete_product(db=db, product_id=product_id)
