from fastapi import APIRouter, HTTPException
from pydantic.v1 import ValidationError
from starlette import status

from models import ErrorMessage
from .models import PaginatedUsersResponse, CreateUserRequest
from .service import get_active_users, create_user, get_user_by_email

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get("", response_model=PaginatedUsersResponse)
def get_all_users():
    return get_active_users()


@router.post("", status_code=status.HTTP_201_CREATED)
def add_user(create_user_request: CreateUserRequest):
    return create_user(create_user_request=create_user_request)


@router.get("/{email}", status_code=status.HTTP_200_OK,responses={404: {"model": ErrorMessage}})
def get_user(email: str):
    try:
        return get_user_by_email(email=email.lower())
    except ValidationError as ve:
        raise HTTPException(status_code=400, detail=f"Validation error: {ve}")


@router.put("/{email}", status_code=status.HTTP_202_ACCEPTED)
def update_user(email: str):
    return ""


@router.delete("/{email}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(email: str):
    return ""
