from typing import Optional
from pydantic import BaseModel, ConfigDict
import uuid
from datetime import datetime

class TripItemCreate(BaseModel):
    trip_id: uuid.UUID
    gear_item_id: uuid.UUID

    quantity: int = 1
    is_packed: bool = False
    
    recorded_weight: Optional[int] = None
    recorded_name: Optional[str] = None

class TripItemUpdate(BaseModel):
    quantity: Optional[int] = None
    is_packed: Optional[bool] = None
    recorded_weight: Optional[int] = None
    recorded_name: Optional[str] = None

class TripItemResponse(BaseModel):
    id: uuid.UUID
    trip_id: uuid.UUID
    gear_item_id: Optional[uuid.UUID]

    quantity: int
    recorded_weight: int
    recorded_name: str
    is_packed: bool

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

