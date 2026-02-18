from fastapi import FastAPI

from app.routers import router1

app = FastAPI(title="Backend API", version="0.1.0")

app.include_router(router1.router, prefix="/router1", tags=["router1"])
