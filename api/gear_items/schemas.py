from typing import Optional
from pydantic import BaseModel, ConfigDict, Field
import uuid
from datetime import datetime

class GearItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    category_id: uuid.UUID
    brand: Optional[str] = Field(None, max_length=255)
    weight_grams: int = 0
    description: Optional[str] = None
    is_consumable: bool = False
    is_worn: bool = False

class GearItemUpdate(BaseModel):
    #Fields are marked as optional since we have patch (partial update) instead of put
    name: Optional[str] = Field(None, min_length=1, max_length=255)
    category_id: Optional[uuid.UUID] = None
    brand: Optional[str] = Field(None, max_length=255)
    weight_grams: Optional[int] = None
    description: Optional[str] = None
    is_consumable: Optional[bool] = None
    is_worn: Optional[bool] = None

class GearItemResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    category_id: uuid.UUID
    name: str = Field(..., min_length=1, max_length=255)
    brand: Optional[str] = Field(None, max_length=255)
    weight_grams: int
    description: Optional[str]
    is_consumable: bool
    is_worn: bool

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)