import uuid

from sqlalchemy import Text, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ModifierOption(Base):
    __tablename__ = "modifier_options"

    id: Mapped[int] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey("modifier_groups.id"), nullable=False)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    price_delta: Mapped[int] = mapped_column(Integer, nullable=False)
    is_available: Mapped[bool] = mapped_column(Boolean, default=False)
    
    group = relationship("ModifierGroup", back_populates="options")
    order_item_modifiers = relationship("OrderItemModifier", back_populates="modifier_option")
