from pydantic import BaseModel
from datetime import datetime as dt


class ProductBase(BaseModel):
    name: str
    image: str
    brand: str
    description: str
    rating: int = 0
    price: int = 0
    count_in_stock: int = 0


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    updated_at: dt
    created_at: dt
    user_id: int

    class Config:
        from_attributes = True
