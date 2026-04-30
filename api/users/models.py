from datetime import datetime
from typing import Optional, List, TYPE_CHECKING
import uuid

from sqlalchemy import String, DateTime, Boolean, Enum, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.core.database import Base, TimestampMixin
from api.core.enums import WeightUnit

if TYPE_CHECKING:
    from api.categories.models import Category
    from api.gear_items.models import GearItem
    from api.trips.models import Trip

class User(Base, TimestampMixin):
    __tablename__ = "users"

    #Primary Key
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)

    #User Attributes
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))

    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    
    is_active: Mapped[bool] = mapped_column(Boolean, server_default="true")

    # TODO: Change location of this as needed
    weight_unit: Mapped[WeightUnit] = mapped_column(
        Enum(WeightUnit),
        default=WeightUnit.GRAMS,
        server_default=WeightUnit.GRAMS.value,
    )

    #Relationships
    categories: Mapped[List["Category"]] = relationship(back_populates="user")
    gear_items: Mapped[List["GearItem"]] = relationship(back_populates="user")
    trips: Mapped[List["Trip"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"<User(username={self.username}, email={self.email})>"