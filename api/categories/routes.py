from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from api.categories.models import Category
from api.categories.schemas import CategoryResponse, CategoryCreate, CategoryUpdate
from api.core.database import get_db
from api.auth.dependencies import get_current_user

router = APIRouter()

# CREATE CATEGORY
@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_category = Category(**category.model_dump())
    # db_category.user

@router.get("", response_model=List[CategoryResponse])
async def get_all(db: Session = Depends(get_db)):
    return db.query(Category).all()

