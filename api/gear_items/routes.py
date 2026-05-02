from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from api.core.database import get_db
from api.auth.dependencies import get_current_user
from api.core.exceptions import raise_404
from api.users.models import User
from api.gear_items.models import GearItem
from api.gear_items.schemas import GearItemResponse, GearItemCreate, GearItemUpdate
from typing import List
import uuid

router = APIRouter()

# CREATE GEAR ITEM
@router.post("/", status_code=201, response_model=GearItemResponse)
async def create_gear_item(gear_item: GearItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_gear_item = GearItem(**gear_item.model_dump())
    db_gear_item.user_id = current_user.id
    db.add(db_gear_item)
    db.commit()
    db.refresh(db_gear_item)
    return db_gear_item

# GET ALL GEAR ITEMS
@router.get("/", response_model=List[GearItemResponse])
async def get_all_gear_items(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.execute(
        select(GearItem).where(
            GearItem.user_id == current_user.id)
        ).scalars().all()

# GET SINGLE GEAR ITEM
@router.get("/{id}", response_model=GearItemResponse)
async def get_gear_item(id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_gear_item = db.execute(
        select(GearItem).where(
            GearItem.id == id,
            GearItem.user_id == current_user.id)
        ).scalar_one_or_none()
    
    if not db_gear_item:
        raise_404("Gear item not found")
    
    return db_gear_item

# UPDATE GEAR ITEM
#Patch allows the gear item to be partially updated which is why it was chosen over put
@router.patch("/{id}", response_model=GearItemResponse)
async def update_gear_item(id: uuid.UUID, gear_item: GearItemUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_gear_item = db.execute(
        select(GearItem).where(
            GearItem.id == id,
            GearItem.user_id == current_user.id)
        ).scalar_one_or_none()

    if not db_gear_item:
        raise_404("Gear item not found")
    
    update_data = gear_item.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_gear_item, field, value)
    
    db.commit()
    db.refresh(db_gear_item)
    return db_gear_item

# DELETE GEAR ITEM
@router.delete("/{id}", status_code=204)
async def delete_gear_item(id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_gear_item = db.execute(
        select(GearItem).where(
            GearItem.id == id,
            GearItem.user_id == current_user.id)
        ).scalar_one_or_none()

    if not db_gear_item:
        raise_404("Gear item not found")
    
    db.delete(db_gear_item)
    db.commit()

    return None