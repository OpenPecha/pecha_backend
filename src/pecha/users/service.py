import jwt
from fastapi.responses import JSONResponse
from fastapi import HTTPException

from config import PECHA_JWT_SECRET, PECHA_JWT_ALG, PECHA_JWT_ISSUER, PECHA_JWT_AUD, PECHA_JWT_EXP
from database.core import SessionLocal
from . import repository
from users.models import PaginatedUsersResponse, UserDTO, CreateUserRequest, Users, UserLoginRequest, UserLoginResponse
from starlette import status
from passlib.context import CryptContext
from datetime import timezone, datetime, timedelta

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_active_users(page: int = 0, per_page: int = 1) -> PaginatedUsersResponse:
    db_session = SessionLocal()
    try:
        offset = page * per_page
        active_users, total_count = repository.find_users_by_active(db=db_session, offset=offset, per_page=per_page)
        user_list = [UserDTO.model_validate(user) for user in active_users]
        return PaginatedUsersResponse(
            per_page=per_page,
            page=page,
            total=total_count,
            users=user_list

        )

    finally:
        db_session.close()


def create_user(create_user_request: CreateUserRequest):
    db_session = SessionLocal()
    try:
        new_user = Users(**create_user_request.model_dump())
        hashed_password = bcrypt_context.hash(create_user_request.password)
        new_user.password = hashed_password
        repository.save_user(db=db_session, user=new_user)
    finally:
        db_session.close()


def authenticate_and_generate_token(user_login_request: UserLoginRequest):
    try:
        current_user = authenticate_user(email=user_login_request.email, password=user_login_request.password)
        full_name = f"{current_user.first_name} {current_user.last_name}"
        access_token = generate_token(email=current_user.email, name=full_name, user_name=current_user.username,
                                      is_admin=current_user.is_admin)
        return UserLoginResponse(
            token=access_token,
            token_type='Bearer'

        )
    except HTTPException as http_exception:
        return JSONResponse(status_code=http_exception.status_code,
                            content={"message": http_exception.detail})


def generate_token(email: str, name: str, user_name: str, is_admin: bool):
    now = datetime.now(timezone.utc)
    expires = (now + timedelta(seconds=PECHA_JWT_EXP)).timestamp()
    data = {
        "sub": email,
        "name": name,
        "username": user_name,
        "iss": PECHA_JWT_ISSUER,
        "aud": PECHA_JWT_AUD,
        "iat": now,
        "exp": expires,
        "is_admin": is_admin
    }
    return jwt.encode(data, PECHA_JWT_SECRET, algorithm=PECHA_JWT_ALG)


def authenticate_user(email: str, password: str):
    db_session = SessionLocal()
    try:
        optional_user = repository.find_user_by_email(db=db_session, email=email)
        is_valid = bcrypt_context.verify(password, optional_user.password)
        if not optional_user or not is_valid:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Email or password is not match')

        return optional_user
    finally:
        db_session.close()


def get_user_by_email(email: str):
    db_session = SessionLocal()
    try:
        optional_user = repository.find_user_by_email(db=db_session, email=email)
        if not optional_user:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "User not found"})
        return UserDTO.model_validate(optional_user)
    finally:
        db_session.close()
