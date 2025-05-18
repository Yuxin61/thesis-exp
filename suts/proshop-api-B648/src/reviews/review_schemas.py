from pydantic import BaseModel
from datetime import datetime as dt

"""`reviews` tables"""


class ReviewBase(BaseModel):
    name: str
    rating: int
    comment: str


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
    user_id: int
    updated_at: dt
    created_at: dt

    class Config:
        from_attributes = True
