import socket
from fastapi import APIRouter
from src.client.hitokoto_client import HITOClient

router = APIRouter()
# init related http client
hitokoto_client = HITOClient()


@router.get("/hitokoto/result")
async def get_random_result():
    try:
        res = hitokoto_client.get_single_result()
        return {"result": "success", "message": "", "data": res, "host": socket.gethostname()}

    except Exception as e:
        return {"result": "error", "message": str(e), "data": [], "host": socket.gethostname()}
