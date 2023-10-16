from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from src.env import ASYNC_DB_CONNECT, SYNC_DB_CONNECT

sync_engine = create_engine(SYNC_DB_CONNECT)  # for create table
engine = create_async_engine(ASYNC_DB_CONNECT)  # for queries
async_session = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)
app = FastAPI()
