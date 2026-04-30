from typing import Optional, TYPE_CHECKING
from datetime import datetime, timezone
import uuid

from sqlalchemy import String, UUID, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from api.core.database import Base, TimestampMixin

if TYPE_CHECKING:
    from api.trips.models import Trip
    from api.gear_items.models import GearItem

class TripItem(Base, TimestampMixin):
    __tablename__ = "trip_items"

    #Primary Key
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)

    #Foreign Keys
    trip_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("trips.id"), ondelete="CASCADE")
    #Making gear_item_id optional allows for the gear item to be deleted without deleting the tripitem
    gear_item_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("gear_items.id"), ondelete="SET NULL")

    #Trip Attributes
    quantity: Mapped[int] = mapped_column(server_default="1", default=1)
    recorded_weight: Mapped[int] = mapped_column(server_default="0", default=0)
    recorded_name: Mapped[str] = mapped_column(String(255), index=True)
    is_packed: Mapped[bool] = mapped_column(Boolean, server_default="false", default=False)

    #Relationships
    trip: Mapped["Trip"] = relationship(back_populates="trip_items")
    gear_item: Mapped[Optional["GearItem"]] = relationship(back_populates="trip_items")

    def __repr__(self) -> str:
        return f"<TripItem(name={self.recorded_name}, qty={self.quantity})>"