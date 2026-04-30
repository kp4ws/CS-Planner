from datetime import datetime, timezone
from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from api.core.database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    #TODO: Add in V2 --> user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(String, unique=True, nullable=False)
    date_created = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))