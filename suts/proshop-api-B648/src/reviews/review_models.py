from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime as dt

from ..database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    rating = Column(Integer, index=True)
    comment = Column(String, index=True)
    updated_at = Column(DateTime, default=dt.utcnow, onupdate=dt.utcnow)
    created_at = Column(DateTime, default=dt.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="reviews")
