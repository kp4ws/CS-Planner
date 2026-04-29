from api.core.database import Base

class TripItem(Base):
    __tablename__ = "trip_items"

#     # In the TripItem model
# trip_id = Column(UUID, ForeignKey("trips.id", ondelete="CASCADE"))
# gear_item_id = Column(UUID, ForeignKey("gear_items.id", ondelete="SET NULL"), nullable=True)