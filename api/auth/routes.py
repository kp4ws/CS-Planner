from fastapi import APIRouter
from auth.schemas import LoginRequest, RegisterRequest

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(request: LoginRequest):
    return {"username": request.username, "password": request.password}

@router.post("/register")
async def register(request: RegisterRequest):
    return {"username": request.username, "password": request.password}