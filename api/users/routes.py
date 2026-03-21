from fastapi import APIRouter, Depends
from auth.dependencies import get_current_user
from users.models import User
from users.schemas import UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user