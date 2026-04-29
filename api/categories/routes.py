from fastapi import APIRouter, Depends
from categories.models import Category
from categories.schemas import CategoryResponse, CategoryCreate, CategoryUpdate
from typing import List
from sqlalchemy.orm import Session
from api.core.database import get_db

router = APIRouter(prefix="/categories", tags=["categories"])

@router.get("", response_model=List[CategoryResponse])
async def get_all(db: Session = Depends(get_db)):
    return db.query(Category).all()

