from typing import Annotated

from fastapi import FastAPI, Depends
from app.db.base import init_db, get_session, AsyncSession
from app.schemas import OrderTime

app = FastAPI()
sessionDep = Annotated[AsyncSession, Depends(get_session)]



@app.get("/create_tables")
async def read_root():
    await init_db()
    return {"message": "Tables created successfully!"}


@app.post("/set_order_time")
async def set_order_time(data: , session: sessionDep):
    
    pass