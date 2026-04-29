from fastapi import APIRouter, Depends, HTTPException
from auth.utils import hash_password, verify_password, create_access_token
from sqlalchemy.orm import Session
from api.core.database import get_db
from users.models import User
from users.schemas import UserLogin, UserCreate, UserResponse
from auth.schemas import TokenResponse

router = APIRouter()

@router.post("/login", response_model=TokenResponse)
async def login(request: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()

    if user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    correct_password = verify_password(request.password, user.password)
    if not correct_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", status_code=201, response_model=UserResponse)
async def register(request: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(request.password)

    #Check if user is already in database
    existing_user = db.query(User).filter(User.username == request.username).first()

    if existing_user:
        raise HTTPException(status_code=409, detail="Username already exists")

    new_user = User(
        username=request.username,
        password=hashed_password,
        email=request.email
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user