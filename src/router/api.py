from fastapi import APIRouter
from src.router import base

API_PREFIX = "/api"

router = APIRouter()
router.include_router(base.router, tags=["basic"], prefix=API_PREFIX)
