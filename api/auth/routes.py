from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.auth.utils import hash_password, verify_password, create_access_token
from api.core.database import get_db
from api.core.exceptions import raise_401, raise_409
from api.users.models import User
from api.users.schemas import UserLogin, UserCreate, UserResponse
from api.auth.schemas import TokenResponse

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
async def login(request: UserLogin, db: Session = Depends(get_db)):
    user = db.execute(
        select(User).where(
            User.username == request.username
        )).scalar_one_or_none()

    if not user:
        raise_401("Incorrect username or password")
    
    correct_password = verify_password(request.password, user.password_hash)
    if not correct_password:
        raise_401("Incorrect username or password")

    access_token = create_access_token({"sub": str(user.id)})

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", status_code=201, response_model=UserResponse)
async def register(request: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(request.password)

    #Check if user is already in database
    existing_user = db.execute(
        select(User).where(
            ((User.username == request.username) | (User.email == request.email))
        )).scalar_one_or_none()

    if existing_user:
        raise_409("A user with this username or email already exists")

    new_user = User(
        username=request.username,
        password_hash=hashed_password,
        email=request.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user