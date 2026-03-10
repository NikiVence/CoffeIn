import uuid

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class OrderItemModifier(Base):
    __tablename__ = "order_item_modifiers"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    order_item_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("order_items.id"), nullable=False)
    modifier_option_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("modifier_options.id"), nullable=False)
    price_delta: Mapped[int] = mapped_column(Integer, nullable=False)

    order_item = relationship("OrderItem", back_populates="modifiers")
    modifier_option = relationship("ModifierOption")