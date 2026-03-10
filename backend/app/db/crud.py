from sqlalchemy import select, update, delete
from app.db.base import get_session
from app.models import *

async def get_shop_work_time(shop_id: int):
    async with get_session() as session:
        result = await session.execute(
            select(CoffeeShop).where(CoffeeShop.id == shop_id)
        )
        shop = result.scalar_one_or_none()
        if shop:
            return shop.opening_time, shop.closing_time
        return None