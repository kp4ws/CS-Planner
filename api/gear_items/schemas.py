from pydantic import BaseModel
from datetime import datetime

# TODO: Need to finish off schema

class GearItemCreate(BaseModel):
    name: str
    # category_id = ForeignKey() TODO: Do we have both id and string or what
    brand: str
    weight: int
    weight_unit: str
    notes: str

class GearItemUpdate(BaseModel):
    name: str
    brand: str
    weight: int
    weight_unit: str
    notes: str

class GearItemResponse(BaseModel):
    name: str
    brand: str
    weight: int
    weight_unit: str
    notes: str