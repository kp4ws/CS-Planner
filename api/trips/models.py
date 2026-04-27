from sqlalchemy import Column, Integer
from datetime import datetime, timezone
from database import Base

class Trip(Base):
    __tablename__ = "trips"