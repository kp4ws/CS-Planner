from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from api.auth.dependencies import get_current_user
from api.users.models import User
from api.users.schemas import UserResponse, UserUpdate
from api.core.database import get_db
from api.core.exceptions import raise_400, raise_409

router = APIRouter()

#GET CURRENT USER
@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user

#UPDATE CURRENT USER
@router.patch("/me", response_model=UserResponse)
async def update_me(request: UserUpdate, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    update_data = request.model_dump(exclude_unset=True)
    
    if not update_data:
        raise_400("No update data provided")

    for field, value in update_data.items():
        setattr(current_user, field, value)
    
    try:
        db.commit()
        db.refresh(current_user)
    except IntegrityError:
        db.rollback()
        raise_409("Username or Email already exists")

    return current_user

#DELETE CURRENT USER
@router.delete("/me")
async def delete_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    current_user.is_active = False
    db.commit()

    return {"message": "User deactivated successfully"}