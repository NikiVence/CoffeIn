from pydantic import BaseModel, Field
from datetime import time

from app.db.crud import get_shop_work_time

class OrderTime(BaseModel):
    async def validate_order_time(self, shop_id: int):
        open_time, close_time = await get_shop_work_time(shop_id)
        if not (open_time <= self.order_time <= close_time):
            raise ValueError("Order time is outside of shop working hours")
        
        order_id: int = Field(..., description="The ID of the order")
        order_time: time = Field(..., description="The time to set for the order")

        