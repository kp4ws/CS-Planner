from fastapi import APIRouter
from sqlalchemy import select
from api.core.dependencies import DBSession, CurrentUser
from api.core.exceptions import raise_404
from api.trips.models import Trip
from api.trips.schemas import TripResponse, TripCreate, TripUpdate
import uuid

router = APIRouter()

#CREATE TRIP
@router.post("", status_code=201, response_model=TripResponse)
async def create_trip(trip: TripCreate, db: DBSession, current_user: CurrentUser):
    db_trip = Trip(**trip.model_dump())
    db_trip.user_id = current_user.id
    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)
    return db_trip

#GET ALL TRIPS
@router.get("", response_model=list[TripResponse])
async def get_all_trips(db: DBSession, current_user: CurrentUser):
    return db.execute(
        select(Trip).where(
            Trip.user_id == current_user.id
        )).scalars().all()

#GET SINGLE TRIP
@router.get("/{id}", response_model=TripResponse)
async def get_trip(id: uuid.UUID, db: DBSession, current_user: CurrentUser):
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
async def update_trip(id: uuid.UUID, trip: TripUpdate, db: DBSession, current_user: CurrentUser):
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
@router.delete("/{id}", status_code=204)
async def delete_trip(id: uuid.UUID, db: DBSession, current_user: CurrentUser):
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

    return None
