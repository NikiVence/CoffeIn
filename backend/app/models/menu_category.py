import uuid

from sqlalchemy import Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class MenuCategory(Base):
    __tablename__ = "menu_categories"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    coffee_shop_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("coffee_shops.id"), nullable=False)
    name: Mapped[str] = mapped_column(Text, nullable=False)

    coffee_shop = relationship("CoffeeShop", back_populates="categories")
    menu_items = relationship("MenuItem", back_populates="category")