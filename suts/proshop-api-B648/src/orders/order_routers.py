from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import order_crud as crud
from .order_schemas import Order, OrderCreate
from ..database import get_db

router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Order not found"}},
)


@router.get("/", response_model=List[Order], summary="Get all orders")
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, skip=skip, limit=limit)
    return orders


@router.get("/id/{order_id}", response_model=Order, summary="Get order by id")
def read_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order


@router.post("/", response_model=Order, summary="Create order")
def create_order(order: OrderCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order, user_id=user_id)


@router.put("/id/{order_id}", response_model=Order, summary="Update order")
def update_order(order_id: int, order: OrderCreate, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return crud.update_order(db=db, order=order, order_id=order_id)


@router.delete("/id/{order_id}", response_model=Order, summary="Delete order")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.get_order(db, order_id=order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return crud.delete_order(db=db, order_id=order_id)
