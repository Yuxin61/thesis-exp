from datetime import datetime as dt
from sqlalchemy.orm import Session

from .product_models import Product
from .product_schemas import ProductCreate


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Product).order_by(Product.id.asc()).offset(skip).limit(limit).all()


def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()


def create_product(db: Session, product: ProductCreate, user_id: int):
    db_product = Product(**product.dict(), user_id=user_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, product_id: int, product: ProductCreate):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        return None
    update_data = product.dict(exclude_unset=True)
    update_data['updated_at'] = dt.utcnow()
    for key, value in update_data.items():
        setattr(db_product, key, value)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product
