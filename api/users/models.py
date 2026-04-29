from datetime import datetime
from typing import Optional

from sqlalchemy import String, DateTime, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column

from api.core.database import Base, TimestampMixin
from api.core.enums import WeightUnit

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True), nullable=True)
    
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    # TODO: Change location of this as needed
    weight_unit: Mapped[WeightUnit] = mapped_column(
        Enum(WeightUnit),
        default=WeightUnit.GRAMS
    )
    
    def __repr__(self) -> str:
        return f"<User(username={self.username}, email={self.email})>"