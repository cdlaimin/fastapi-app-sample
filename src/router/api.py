from fastapi import APIRouter
from src.router import animal, tools

API_PREFIX = "/api"

router = APIRouter()
router.include_router(animal.router, tags=["animal"], prefix=API_PREFIX + "/animal")
router.include_router(tools.router, tags=["tools"], prefix=API_PREFIX + "/tools")
