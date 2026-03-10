import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ItemModifierGroup(Base):
    __tablename__ = "item_modifier_groups"
    
    id: Mapped[int] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    menu_item_id: Mapped[int] = mapped_column(UUID(as_uuid=True), ForeignKey("menu_items.id"), nullable=False)
    modifier_group_id: Mapped[int] = mapped_column(UUID(as_uuid=True), ForeignKey("modifier_groups.id"), nullable=False)

    menu_item_id = relationship("MenuItem", back_populates="modifier_groups")
    modifier_group = relationship("ModifierGroup", back_populates="item_modifier_groups")