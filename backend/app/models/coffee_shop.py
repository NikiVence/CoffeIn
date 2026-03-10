import uuid
from datetime import datetime
from typing import List
from sqlalchemy import Boolean, Text, Time, DateTime, DECIMAL, Integer, ARRAY
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class CoffeeShop(Base):
    __tablename__ = "coffee_shops"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    owners: Mapped[List[int]] = mapped_column(ARRAY(Integer), nullable=False)

    opening_time: Mapped[datetime.time] = mapped_column(Time, nullable=False)
    closing_time: Mapped[datetime.time] = mapped_column(Time, nullable=False)

    address: Mapped[str] = mapped_column(Text, nullable=False)
    latitude: Mapped[float] = mapped_column(DECIMAL(9, 6), nullable=False)
    longitude: Mapped[float] = mapped_column(DECIMAL(9, 6), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())


    categories = relationship("MenuCategory", back_populates="coffee_shop")
    menu_items = relationship("MenuItem", back_populates="coffee_shop")
    modifier_groups = relationship("ModifierGroup", back_populates="coffee_shop")
    orders = relationship("Order", back_populates="coffee_shop")