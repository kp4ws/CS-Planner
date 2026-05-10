from fastapi import APIRouter
from sqlalchemy import select
from api.core.dependencies import DBSession, CurrentUser
from api.core.exceptions import raise_404
from api.gear_items.models import GearItem
from api.gear_items.schemas import GearItemResponse, GearItemCreate, GearItemUpdate
import uuid

router = APIRouter()

# CREATE GEAR ITEM
@router.post("", status_code=201, response_model=GearItemResponse)
async def create_gear_item(gear_item: GearItemCreate, db: DBSession, current_user: CurrentUser):
    db_gear_item = GearItem(**gear_item.model_dump())
    db_gear_item.user_id = current_user.id
    db.add(db_gear_item)
    db.commit()
    db.refresh(db_gear_item)
    return db_gear_item

# GET ALL GEAR ITEMS
@router.get("", response_model=list[GearItemResponse])
async def get_all_gear_items(db: DBSession, current_user: CurrentUser):
    return db.execute(
        select(GearItem).where(
            GearItem.user_id == current_user.id)
        ).scalars().all()

# GET SINGLE GEAR ITEM
@router.get("/{id}", response_model=GearItemResponse)
async def get_gear_item(id: uuid.UUID, db: DBSession, current_user: CurrentUser):
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
async def update_gear_item(id: uuid.UUID, gear_item: GearItemUpdate, db: DBSession, current_user: CurrentUser):
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
async def delete_gear_item(id: uuid.UUID, db: DBSession, current_user: CurrentUser):
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
