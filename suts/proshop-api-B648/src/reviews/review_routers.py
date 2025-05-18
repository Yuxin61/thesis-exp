from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import review_crud as crud
from .review_schemas import Review, ReviewCreate
from ..database import get_db

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
    responses={404: {"description": "Review not found"}},
)
