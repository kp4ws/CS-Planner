from pydantic import BaseModel
from typing import Optional

class UserLogin(BaseModel):
    username : str
    password : str

class UserCreate(BaseModel):
    username: str
    password: str
    email: str

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    
    class Config:
        from_attributes = True