from typing import Optional
from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime

class TripCreate(BaseModel):
    name: str
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None

class TripUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[datetime] = None

class TripResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    name: str
    description: Optional[str]
    location: Optional[str]
    start_date: Optional[datetime]

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

