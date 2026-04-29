from api.core.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime, timezone

class GearItem(Base):
    __tablename__ = "gear_items"

    id = Column(Integer, primary_key=True, index=True)
    name = String()
    category_id = ForeignKey()
    brand = String()
    weight = Integer()
    weight_unit = String()
    notes = String()