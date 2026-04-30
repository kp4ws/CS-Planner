from typing import Optional
from datetime import datetime
import uuid

from pydantic import BaseModel, ConfigDict

class CategoryCreate(BaseModel):
    title: str

class CategoryUpdate(BaseModel):
    title: Optional[str] = None

class CategoryResponse(BaseModel):
    id: uuid.UUID
    user_id: uuid.UUID
    title: str
    deleted_at: Optional[datetime]
    is_default: bool
    # icon: Mapped[str] = mapped_column() TODO: Add in later iteration

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)