
from pydantic import BaseModel, EmailStr, constr


class UserLoginResponse(BaseModel):
    token: str
    token_type: str


class UserLoginRequest(BaseModel):
    email: EmailStr
    password: constr(min_length=8, max_length=20)
