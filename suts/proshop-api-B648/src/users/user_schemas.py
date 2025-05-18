from datetime import datetime as dt
from pydantic import BaseModel
from typing import List

from src.products import Product

"""`users` tables"""


class UserBase(BaseModel):
    name: str
    email: str
    password: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    is_admin: bool = False


class User(UserBase):
    id: int
    is_admin: bool = False
    products: List[Product] = []
    updated_at: dt
    created_at: dt

    class Config:
        from_attributes = True
