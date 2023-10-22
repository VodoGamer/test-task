from src.client import app, engine
from src.routers import routers
from src.services.db.models import Base

for router in routers:
    app.include_router(router)


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


__all__ = ("app",)
