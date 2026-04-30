from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from api.core.database import get_db
from api.core.exceptions import raise_404
from api.gear_items.models import GearItem
from api.gear_items.schemas import GearItemResponse, GearItemCreate, GearItemUpdate
from typing import List

router = APIRouter()

# CREATE GEAR ITEM
@router.post("/", response_model=GearItemResponse)
async def create_gear_item(gear_item: GearItemCreate, db: Session = Depends(get_db)):
    # TODO: Need to attach user_id to gear item
    # db_gear_item.user_id = current_user["user_id"]
    db_gear_item = GearItem(**gear_item.model_dump())
    db.add(db_gear_item)
    db.commit()
    db.refresh(db_gear_item)
    return db_gear_item

# READ ALL GEAR ITEMS
@router.get("/", response_model=List[GearItemResponse])
async def get_all_gear_items(db: Session = Depends(get_db)):
    # TODO: Filter gear items by user id so only gear items belonging to each user are returned
    return db.execute(select(GearItem)).scalars().all()

# READ SINGLE GEAR ITEM
@router.get("/{id}", response_model=GearItemResponse)
async def get_gear_item(id: str, db: Session = Depends(get_db)):
    #TODO: Filter gear items by user id
    db_gear_item = db.execute(select(GearItem).where(GearItem.id == id)).scalar_one_or_none()
    
    if not db_gear_item:
        raise_404("Gear item not found")
    
    return db_gear_item

# UPDATE GEAR ITEM
#TODO: Consider changing from put to patch
@router.put("/{id}", response_model=GearItemResponse)
async def update_gear_item(id: str, gear_item: GearItemUpdate, db: Session = Depends(get_db)):
    db_gear_item = db.execute(select(GearItem).where(GearItem.id == id)).scalar_one_or_none()

    if not db_gear_item:
        raise_404("Gear item not found")
    
    update_data = gear_item.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_gear_item, field, value)
    
    db.commit()
    db.refresh(db_gear_item)
    return db_gear_item

# DELETE GEAR ITEM
@router.delete("/{id}")
async def delete_gear_item(id: str, db: Session = Depends(get_db)):
    db_gear_item = db.execute(select(GearItem).where(GearItem.id == id)).scalar_one_or_none()

    if not db_gear_item:
        raise_404("Gear item not found")
    
    db.delete(db_gear_item)
    db.commit()

    return {"message": "Item deleted"}