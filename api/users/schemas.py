from typing import Optional
from datetime import datetime
import uuid
from pydantic import BaseModel, ConfigDict, EmailStr, Field
from api.core.enums import WeightUnit

class UserLogin(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    password : str

class UserCreate(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    password: str
    email: EmailStr = Field(..., max_length=255)

class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=1, max_length=50)
    email: Optional[EmailStr] = Field(None, max_length=255)
    weight_unit: Optional[WeightUnit] = None

class UserResponse(BaseModel):
    id: uuid.UUID
    username: str = Field(..., min_length=1, max_length=50)
    email: EmailStr = Field(..., max_length=255)
    last_login: Optional[datetime]
    is_active: bool
    weight_unit: WeightUnit

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)