from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter
from starlette import status

from auth.models import UserLoginResponse, UserLoginRequest

auth_router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)

