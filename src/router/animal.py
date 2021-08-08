import socket
from fastapi import APIRouter
from src.client.cats_client import CatClient

router = APIRouter()
# init related http client
cat_client = CatClient()


@router.get("/cats/tags")
async def get_all_tags():
    try:
        res = cat_client.get_all_tags()
        return {"result": "success", "message": "", "data": res, "host": socket.gethostname()}

    except Exception as e:
        return {"result": "error", "message": str(e), "data": [], "host": socket.gethostname()}
