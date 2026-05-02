from typing import Optional
from datetime import datetime
import uuid
from pydantic import BaseModel, ConfigDict, EmailStr
from api.core.enums import WeightUnit

class UserLogin(BaseModel):
    username : str
    password : str

class UserCreate(BaseModel):
    username: str 
    password: str
    email: EmailStr

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    weight_unit: Optional[WeightUnit] = None

class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr
    last_login: Optional[datetime]
    is_active: bool
    weight_unit: WeightUnit

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)