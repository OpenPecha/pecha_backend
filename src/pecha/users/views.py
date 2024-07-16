from fastapi import APIRouter

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get("")
def get_users():
    """Get list of all Active users """
    return ""

@router.post("")
def create_user():
    """"""
    return ""

@router.get("/{email}")
def get_user(email: str):
    return ""
@router.put("/{email}")
def update_user(email: str):
    return ""