from fastapi import APIRouter
from app.api.routes import api_router

api = APIRouter()
api.include_router(api_router)