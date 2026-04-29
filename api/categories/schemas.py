from pydantic import BaseModel
from datetime import datetime

class CategoryCreate(BaseModel):
    title: str

class CategoryUpdate(BaseModel):
    title: str

class CategoryResponse(BaseModel):
    id: int
    title: str
    created_at: datetime

    class Config:
        from_attributes = True