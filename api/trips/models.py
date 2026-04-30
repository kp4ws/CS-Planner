from typing import Optional, List, TYPE_CHECKING
from datetime import datetime, timezone
import uuid

from sqlalchemy import String, UUID, ForeignKey, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.core.database import Base, TimestampMixin

if TYPE_CHECKING:
    from api.users.models import User
    from api.trip_items.models import TripItem

class Trip(Base, TimestampMixin):
    __tablename__ = "trips"

    #Primary Key
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)

    #Foreign Keys
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))

    #Trip Attributes
    name: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[Optional[str]] = mapped_column(Text(500))
    location: Mapped[Optional[str]] = mapped_column(String(255))
    start_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    #Relationships
    user: Mapped["User"] = relationship(back_populates="trips")
    #cascade allows us to delete any trip items belonging to this trip upon deletion of this trip
    trip_items: Mapped[List["TripItem"]] = relationship(back_populates="trip", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"<Trip(name={self.name})>"