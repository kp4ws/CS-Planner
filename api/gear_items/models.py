from typing import Optional
import uuid

from sqlalchemy import String, ForeignKey, Text, Boolean, UUID
from sqlalchemy.orm import Mapped, mapped_column

from api.core.database import Base, TimestampMixin

class GearItem(Base, TimestampMixin):
    __tablename__ = "gear_items"

    #Primary Key
    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)

    #Foreign Keys
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    category_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("categories.id"))

    #GearItem Attributes
    name: Mapped[str] = mapped_column(String(255), index=True)
    brand: Mapped[Optional[str]] = mapped_column(String(255))
    weight_grams: Mapped[int] = mapped_column(server_default="0") #TODO: Figure out if I should store None or 0 as default state
    # weight_unit = String() TODO: Figure out which location this should go
    description: Mapped[Optional[str]] = mapped_column(Text(500))
    is_consumable: Mapped[bool] = mapped_column(Boolean, server_default="false")
    is_worn: Mapped[bool] = mapped_column(Boolean, server_default="false")

    def __repr__(self) -> str:
        return f"<GearItem(name={self.name}, brand={self.brand}, description={self.description})>"