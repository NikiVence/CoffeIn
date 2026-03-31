from typing import Annotated

from fastapi import FastAPI, Depends, Query
from schemas import OrderTime, CoffeeShopResponse, CoffeeShopMenu, MenuCategoryResponse, AddToCartRequest, RemoveFromCartRequest, CartResponse
from db.cache import crud_redis_time_order
from db.crud import get_all_coffee_shops, get_coffee_shop_menu as get_coffee_shop_menu_db, add_to_cart, remove_from_cart, get_cart

from typing import List

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/set_order_time")
async def set_order_time(data: OrderTime):
    result = await crud_redis_time_order(
        tg_id=data.tg_id,
        date=data.date,
        action=data.action
    )
    return result

@app.get("/coffee_shops", response_model=List[CoffeeShopResponse])
async def get_coffee_shops():
    shops = await get_all_coffee_shops()
    return shops

@app.get("/menu", response_model=List[MenuCategoryResponse])
async def get_coffee_shop_menu_handler(id: str = Query(..., description="ID кофейни")):
    categories = await get_coffee_shop_menu_db(id)
    return categories



@app.post("/add_to_cart", response_model=CartResponse)
async def add_to_cart_handler(data: AddToCartRequest):
    cart = await add_to_cart(data.tg_id, data.coffee_shop_id, data.menu_item_id, data.quantity)
    if not cart:
        return {"error": "Товар не найден"}
    return cart

@app.post("/remove_from_cart")
async def remove_from_cart_handler(data: RemoveFromCartRequest):
    result = await remove_from_cart(data.tg_id, data.order_item_id)
    if not result:
        return {"error": "Товар не найден"}
    return {"success": True}

@app.get("/get_cart")
async def get_cart_handler(tg_id: int, coffee_shop_id: str):
    from uuid import UUID
    cart = await get_cart(tg_id, UUID(coffee_shop_id))
    if not cart:
        return {"error": "Корзина пуста"}
    return cart