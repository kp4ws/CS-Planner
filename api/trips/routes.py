from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from api.core.database import get_db
from api.auth.dependencies import get_current_user
from api.core.exceptions import raise_404
from api.users.models import User
from api.trips.models import Trip
from api.trips.schemas import TripResponse, TripCreate, TripUpdate
from typing import List
import uuid

router = APIRouter()

#CREATE TRIP
@router.post("/", response_model=TripResponse)
async def create_trip(trip: TripCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_trip = Trip(**trip.model_dump())
    db_trip.user_id = current_user.id
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

#GET ALL TRIPS
@router.get("/", response_model=TripResponse)
async def get_all_trips(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.execute(
        select(Trip).where(
            Trip.user_id == current_user.id
        )).scalars().all()

#GET SINGLE TRIP
@router.get("/{id}", response_model=TripResponse)
async def get_trip(id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_trip = db.execute(
        select(Trip).where(
            Trip.id == id,
            Trip.user_id == current_user.id
        )
    ).scalar_one_or_none()

    if not db_trip:
        raise_404("Trip not found")
    
    return db_trip

#UPDATE TRIP
@router.patch("/{id}", response_model=TripResponse)
async def update_trip(id: uuid.UUID, trip: TripUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_trip = db.execute(
        select(Trip).where(
            Trip.id == id,
            Trip.user_id == current_user.id
        )
    ).scalar_one_or_none()

    if not db_trip:
        raise_404("Trip not found")

    update_data = trip.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_trip, field, value)

    db.commit()
    db.refresh(db_trip)
    return db_trip

#DELETE TRIP
@router.delete("/{id}")
async def delete_trip(id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_trip = db.execute(
        select(Trip).where(
            Trip.id == id,
            Trip.user_id == current_user.id
        )
    ).scalar_one_or_none()

    if not db_trip:
        raise_404("Trip not found")

    db.delete(db_trip)
    db.commit()

    return {"message": "Trip deleted"}