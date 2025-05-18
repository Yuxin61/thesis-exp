from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime as dt

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)
    is_admin = Column(Boolean, default=False)
    updated_at = Column(DateTime, default=dt.utcnow, onupdate=dt.utcnow)
    created_at = Column(DateTime, default=dt.utcnow)

    products = relationship("Product", back_populates="user")
