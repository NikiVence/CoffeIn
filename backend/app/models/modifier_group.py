import uuid

from sqlalchemy import Text, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class ModifireGroup():
    __tablename__ = "modifier_groups"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    coffee_shop_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("coffee_shops.id"), nullable=False)
    
    name: Mapped[str] = mapped_column(Text, nullable=False)
    required: Mapped[bool] = mapped_column(Boolean, default=False)
    multi_select: Mapped[bool] = mapped_column(Boolean, default=False)

    coffee_shop = relationship("CoffeeShop", back_populates="modifier_groups")
    options = relationship("ModifierOption", back_populates="modifier_group", lazy="selectin")
    items = relationship("ItemModifierGroup", back_populates="modifier_group")
