from fastapi import FastAPI
from .database import Base, engine
from .api import endpoints

# Create tables (for dev only — use Alembic in prod!)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(endpoints.router, prefix="/api/v1")
