from fastapi.responses import JSONResponse
from database.core import SessionLocal
from . import repository
from users.models import PaginatedUsersResponse, UserDTO, CreateUserRequest, Users
from starlette import status


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
        repository.save_user(db=db_session, user=new_user)
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
