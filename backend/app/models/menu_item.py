import uuid
from datetime import datetime

from sqlalchemy import Text, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    coffee_shop_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("coffee_shops.id"), nullable=False)
    category_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("menu_categories.id"), nullable=False)

    name: Mapped[str] = mapped_column(Text, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    base_price: Mapped[int] = mapped_column(Integer, nullable=False)
    image_url: Mapped[str] = mapped_column(Text, nullable=True)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    coffee_shop = relationship("CoffeeShop", back_populates="menu_items")
    category = relationship("MenuCategory", back_populates="items")
    modifier_groups = relationship("ItemModifierGroup", back_populates="menu_item", lazy="selectin")
    order_items = relationship("OrderItem", back_populates="menu_item")