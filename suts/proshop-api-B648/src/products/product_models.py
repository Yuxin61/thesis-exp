from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime as dt

from ..database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    image = Column(String, index=True)
    brand = Column(String, index=True)
    description = Column(String, index=True)
    rating = Column(Integer, index=True, default=0)
    price = Column(Integer, index=True, default=0)
    count_in_stock = Column(Integer, index=True, default=0)
    updated_at = Column(DateTime, default=dt.utcnow, onupdate=dt.utcnow)
    created_at = Column(DateTime, default=dt.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="products")
