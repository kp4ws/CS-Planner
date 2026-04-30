from datetime import datetime, timezone
from typing import Optional, List, TYPE_CHECKING
import uuid

from sqlalchemy import UUID, ForeignKey, String, DateTime, Boolean, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.core.database import Base

if TYPE_CHECKING:
    from api.gear_items.models import GearItem
    from api.users.models import User

class Category(Base):
    __tablename__ = "categories"

    __table_args__ = (
        #Allows us to create a unique constraint so that each user must have unique titles
        UniqueConstraint("user_id", "title", name="_user_category_uc"),
    )

    #Primary Key
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)

    #Foreign Key
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    
    #Category Attributes
    title: Mapped[str] = mapped_column(String(100), index=True)
    deleted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    is_default: Mapped[bool] = mapped_column(Boolean, server_default="false")
    # icon: Mapped[str] = mapped_column() TODO: Add in later iteration
    
    #Relationships:
    gear_items: Mapped[List["GearItem"]] = relationship(back_populates="category")
    user: Mapped["User"] = relationship(back_populates="categories")

    def __repr__(self) -> str:
        return f"<Category(title={self.title}, is default={self.is_default})>"