from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=True)
    date_created = Column(DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))