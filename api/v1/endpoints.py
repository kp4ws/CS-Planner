from fastapi import APIRouter
from api.auth.routes import router as auth_router
from api.users.routes import router as user_router
from api.categories.routes import router as category_router
from api.gear_items.routes import router as gear_item_router
from api.trip_items.routes import router as trip_item_router
from api.trips.routes import router as trip_router

v1_router = APIRouter()

v1_router.include_router(
    auth_router,
    prefix="/auth", 
    tags=["Authentication"])

v1_router.include_router(
    user_router,
    prefix="/users", 
    tags=["Users"])

v1_router.include_router(
    category_router,
    prefix="/categories",
    tags=["Categories"]
)

v1_router.include_router(
    gear_item_router,
    prefix="/gear_items",
    tags=["Gear Items"]
)

v1_router.include_router(
    trip_item_router,
    prefix="/trip_items",
    tags=["Trip Items"]
)

v1_router.include_router(
    trip_router,
    prefix="/trips",
    tags=["Trips"]
)