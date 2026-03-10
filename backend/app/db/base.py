import asyncio

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from app.models import *  # важно чтобы модели импортировались


DATABASE_URL = "postgresql+asyncpg://postgres:password@localhost:5432/coffee_db"

class Base(DeclarativeBase):
    pass

engine = create_async_engine(
    DATABASE_URL,
    echo=True,
)


session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

async def get_session():
    async with session_maker() as session:
        yield session

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
