from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from api.users.models import User
from api.categories.models import Category
from api.categories.schemas import CategoryResponse, CategoryCreate, CategoryUpdate
from api.core.database import get_db
from api.core.exceptions import raise_404
from api.auth.dependencies import get_current_user
import uuid

router = APIRouter()

# CREATE CATEGORY
@router.post("/", response_model=CategoryResponse)
async def create_category(category: CategoryCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_category = Category(**category.model_dump())
    db_category.user_id = current_user.id
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

#GET ALL CATEGORIES
@router.get("/", response_model=List[CategoryResponse])
async def get_all_categories(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.execute(
        select(Category).where(
            Category.user_id == current_user.id)
        ).scalars().all()

#GET SINGLE CATEGORY
@router.get("/{id}", response_model=CategoryResponse)
async def get_category(id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_category = db.execute(
        select(Category).where(
            Category.id == id,
            Category.user_id == current_user.id)
    ).scalar_one_or_none()

    if not db_category:
        raise_404("Category not found")

    return db_category

#UPDATE CATEGORY
@router.patch("/{id}", response_model=CategoryResponse)
async def update_category(id: uuid.UUID, category: CategoryUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_category = db.execute(
        select(Category).where(
            Category.id == id,
            Category.user_id == current_user.id
        )
    ).scalar_one_or_none()

    if not db_category:
        raise_404("Category not found")

    update_data = category.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_category, field, value)

    db.commit()
    db.refresh(db_category)
    return db_category

#DELETE CATEGORY
@router.delete("/{id}")
async def delete_category(id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_category = db.execute(
        select(Category).where(
        Category.id == id,
        Category.user_ud == current_user.id
    )).scalar_one_or_none()

    if not db_category:
        raise_404("Category not found")

    #TODO: We want to change this to soft delete, so users can easily delete and add categories
    db.delete(Category)
    db.commit()

    return {"message": "Category deleted"}