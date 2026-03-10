import uuid
from datetime import datetime

from sqlalchemy import Text, Integer, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    telegram_id: Mapped[int] = mapped_column(ForeignKey("users.telegram_id"))
    coffee_shop_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("coffee_shops.id"), nullable=False)
    status: Mapped[str] = mapped_column(Text, default="new")
    total_amount: Mapped[int] = mapped_column(Integer, default=0)
    сreated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    user = relationship("User", back_populates="orders")
    coffee_shop = relationship("CoffeeShop", back_populates="orders")
    items = relationship("OrderItem", back_populates="order", lazy="selectin")