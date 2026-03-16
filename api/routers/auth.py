from fastapi import APIRouter
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username : str
    password : str
    #TODO email

class RegisterRequest(BaseModel):
    username: str
    password: str
    #TODO email

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login(request: LoginRequest):
    return {"username": request.username, "password": request.password}

router.post("/register")
async def register():
    return {"message": "Register endpoint"}