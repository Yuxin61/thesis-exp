from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import user_crud as crud
from .user_schemas import User, UserCreate, UserUpdate
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "User not found"}},
)


@router.get("/", response_model=List[User], summary="Get all users")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/id/{user_id}", response_model=User, summary="Get user by id")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/", response_model=User, summary="Create user")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user=user)
    return db_user


@router.put("/id/{user_id}", response_model=User, summary="Update user")
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db=db, user=user, user_id=user_id)


@router.delete("/id/{user_id}", response_model=User, summary="Delete user")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=user_id)
