from datetime import datetime as dt
from sqlalchemy.orm import Session

from .order_models import Order
from .order_schemas import OrderCreate


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Order).order_by(Order.id.asc()).offset(skip).limit(limit).all()


def get_order(db: Session, order_id: int):
    return db.query(Order).filter(Order.id == order_id).first()


def create_order(db: Session, order: OrderCreate, user_id: int):
    db_order = Order(**order.dict(), user_id=user_id)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def update_order(db: Session, order_id: int, order: OrderCreate):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        return None
    update_data = order.dict(exclude_unset=True)
    update_data['updated_at'] = dt.utcnow()
    for key, value in update_data.items():
        setattr(db_order, key, value)
    db.commit()
    db.refresh(db_order)
    return db_order


def delete_order(db: Session, order_id: int):
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        return None
    db.delete(db_order)
    db.commit()
    return db_order
