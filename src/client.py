from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.env import DB_CONNECT

engine = create_async_engine(DB_CONNECT)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
app = FastAPI()
