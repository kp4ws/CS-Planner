from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
import uuid
from datetime import datetime

class TripCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str] = None
    location: Optional[str] = Field(None, max_length=255)
    start_date: Optional[datetime] = None

class TripUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = None
    location: Optional[str] = Field(None, max_length=255)
    start_date: Optional[datetime] = None

class TripResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    name: str = Field(..., min_length=1, max_length=255)
    description: Optional[str]
    location: Optional[str] = Field(None, max_length=255)
    start_date: Optional[datetime]

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

