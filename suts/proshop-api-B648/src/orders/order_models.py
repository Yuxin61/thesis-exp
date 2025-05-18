from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Table
from sqlalchemy.orm import relationship
from datetime import datetime as dt

from ..database import Base
from .order_status import OrderStatus

orders_products = Table('orders_products', Base.metadata,
                        Column('order_id', Integer, ForeignKey('orders.id')),
                        Column('product_id', Integer, ForeignKey('products.id'))
                        )


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="orders")

    products = relationship("Product", secondary=orders_products, backref="orders")

    status = Column(Enum(OrderStatus), default=OrderStatus.pending)
    quantity = Column(Integer, default=0)
    address = Column(String, index=True)
    phone = Column(String, index=True)
    updated_at = Column(DateTime, default=dt.utcnow, onupdate=dt.utcnow)
    created_at = Column(DateTime, default=dt.utcnow)
