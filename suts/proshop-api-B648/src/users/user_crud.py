from datetime import datetime as dt
from sqlalchemy.orm import Session

from .user_models import User
from .user_schemas import UserCreate, UserUpdate


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).order_by(User.id.asc()).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    update_data = user.dict(exclude_unset=True)
    update_data['updated_at'] = dt.utcnow()
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
