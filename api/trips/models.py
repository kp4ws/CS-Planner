from sqlalchemy import Column, Integer
from datetime import datetime, timezone
from api.core.database import Base

class Trip(Base):
    __tablename__ = "trips"