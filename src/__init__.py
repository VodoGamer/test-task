from src.client import app, sync_engine
from src.routers import routers
from src.services.db.models import Base

for router in routers:
    app.include_router(router)


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(sync_engine)


__all__ = ("app",)
