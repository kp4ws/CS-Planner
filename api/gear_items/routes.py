from fastapi import APIRouter, Depends

router = APIRouter(prefix="/", tags=[""])

@router.get("/", response_model=None)
async def get_all(users):
    return users