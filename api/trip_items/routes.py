from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from api.core.database import get_db
from api.core.exceptions import raise_404
from api.users.models import User
from api.trips.models import Trip
from api.trip_items.models import TripItem
from api.auth.dependencies import get_current_user
from api.trip_items.schemas import TripItemCreate, TripItemUpdate, TripItemResponse
import uuid

router = APIRouter()

#CREATE TRIP ITEM
@router.post("/", status_code=201, response_model=TripItemResponse)
async def create_trip_item(trip_item: TripItemCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Verify the trip belongs to the current user
    db_trip = db.execute(
        select(Trip).where(Trip.id == trip_item.trip_id, Trip.user_id == current_user.id)
    ).scalar_one_or_none()
    
    if not db_trip:
        raise_404("Trip not found")

    db_trip_item = TripItem(**trip_item.model_dump())
    db.add(db_trip_item)
    db.commit()
    db.refresh(db_trip_item)
    return db_trip_item

#GET ALL TRIP ITEMS
@router.get("/", response_model=List[TripItemResponse])
async def get_all_trip_items(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.execute(
        select(TripItem).join(TripItem.trip).where(
            Trip.user_id == current_user.id
        )
    ).scalars().all()

#GET SINGLE TRIP ITEM
@router.get("/{id}", response_model=TripItemResponse)
async def get_trip_item(id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_trip_item = db.execute(
        select(TripItem).join(TripItem.trip).where(
            TripItem.id == id,
            Trip.user_id == current_user.id
        )
    ).scalar_one_or_none()

    if not db_trip_item: 
        raise_404("Trip Item not found")

    return db_trip_item

#UPDATE TRIP ITEM
@router.patch("/{id}", response_model=TripItemResponse)
async def update_trip_item(id: uuid.UUID, trip_item: TripItemUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_trip_item = db.execute(
        select(TripItem).join(TripItem.trip).where(
            TripItem.id == id,
            Trip.user_id == current_user.id
        )
    ).scalar_one_or_none()

    if not db_trip_item: 
        raise_404("Trip Item not found")

    update_data = trip_item.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_trip_item, field, value)

    db.commit()
    db.refresh(db_trip_item)
    return db_trip_item

#DELETE TRIP ITEM
@router.delete("/{id}", status_code=204)
async def delete_trip_item(id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_trip_item = db.execute(
        select(TripItem).join(TripItem.trip).where(
            TripItem.id == id,
            Trip.user_id == current_user.id
        )
    ).scalar_one_or_none()

    if not db_trip_item: 
        raise_404("Trip Item not found")

    db.delete(db_trip_item)
    db.commit()

    return None