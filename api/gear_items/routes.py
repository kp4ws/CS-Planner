from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.core.database import get_db
from gear_items.models import GearItem
from gear_items.schemas import GearItemResponse, GearItemCreate, GearItemUpdate
from typing import List

router = APIRouter(prefix="/gear_items", tags=["gear_items"])

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
    return db.query(GearItem).all()

# READ SINGLE GEAR ITEM
@router.get("/{id}", response_model=GearItemResponse)
async def get_gear_item(id: int, db: Session = Depends(get_db)):
    return db.query(GearItem).filter(GearItem.id == id).first()

# UPDATE GEAR ITEM
@router.put("/{id}", response_model=GearItemUpdate)
async def update_gear_item(id: int, db: Session = Depends(get_db)):
    pass

# DELETE GEAR ITEM
@router.delete("/{id}", response_model=None)
async def delete_gear_item(id: int, db: Session = Depends(get_db)):
    return {"message": "Item deleted"}