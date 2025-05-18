from pydantic import BaseModel
from datetime import datetime as dt
from typing import List

from .order_status import OrderStatus
from src.products import Product


class OrderBase(BaseModel):
    status: OrderStatus = OrderStatus.pending
    quantity: int = 0
    address: str
    phone: str


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    user_id: int
    products: List[Product] = []
    updated_at: dt
    created_at: dt

    class Config:
        from_attributes = True
