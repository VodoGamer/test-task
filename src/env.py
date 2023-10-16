from os import getenv

from dotenv import load_dotenv

load_dotenv()

POSTGRES_USER = getenv("POSTGRES_USER", "postgres")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD", "postgres")
POSTGRES_HOST = getenv("POSTGRES_HOST", "db")
POSTGRES_DB = getenv("POSTGRES_DB", "test_task")

POSTGRES_AUTH = f"{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_DB}"
ASYNC_DB_CONNECT = f"postgresql+asyncpg://{POSTGRES_AUTH}"
SYNC_DB_CONNECT = f"postgresql+psycopg2://{POSTGRES_AUTH}"
