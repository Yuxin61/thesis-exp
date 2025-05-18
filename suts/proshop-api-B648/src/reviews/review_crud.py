from datetime import datetime as dt

from sqlalchemy.orm import Session

from .review_models import Review
from .review_schemas import ReviewCreate


def get_reviews_by_user_id(db: Session, user_id: int):
    return db.query(Review).filter(Review.user_id == user_id).all()


def create_review(db: Session, review: ReviewCreate, user_id: int):
    db_review = Review(**review.dict(), user_id=user_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review


def update_review(db: Session, review: ReviewCreate, review_id: int):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    db_review.name = review.name
    db_review.rating = review.rating
    db_review.comment = review.comment
    db_review.updated_at = dt.now()
    db.commit()
    db.refresh(db_review)
    return db_review


def delete_review(db: Session, review_id: int):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    db.delete(db_review)
    db.commit()
    return db_review
