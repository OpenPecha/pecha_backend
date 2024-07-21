from typing import Optional

from sqlalchemy.orm import Session

from .models import Users


def find_users_by_active(db: Session, offset: int = 0, per_page: int = 10):
    user_query = db.query(Users).filter(Users.is_active == True)
    total_count = user_query.count()
    users = user_query.offset(offset).limit(per_page).all()
    return users, total_count


def save_user(db: Session, user: Users):
    db.add(user)
    db.commit()


def find_user_by_email(db: Session, email: str) -> Optional[Users]:
    return db.query(Users).filter(Users.email == email).first()
