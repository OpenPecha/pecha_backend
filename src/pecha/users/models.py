from _datetime import datetime
import _datetime
from typing import List

from pydantic import BaseModel

from database.core import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean



class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(150), unique=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)
    date_joined = Column(DateTime, default=datetime.now(_datetime.UTC))
    last_login = Column(DateTime, default=None)


class UserDTO(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str

    class Config:
        orm_mode = True
        from_attributes = True


class CreateUserRequest(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str


class PaginatedUsersResponse(BaseModel):
    per_page: int
    page: int
    total: int
    users: List[UserDTO]
