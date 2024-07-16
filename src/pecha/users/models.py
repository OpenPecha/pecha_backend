from _datetime import datetime
import _datetime

from ..db.database import Base
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
