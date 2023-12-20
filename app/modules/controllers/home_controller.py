from datetime import datetime

from aiohttp import web
from aiohttp_session import get_session
from modules.schemas.response_schema import CheckResponse, CheckStatus


async def welcome(request: web.Request):
    """
    ---
    description: This end-point to check server is oke
    tags:
    - Health check
    produces:
    - text/plain
    responses:
        "200":
            description: successful operation. Return "Welcome to home page" text
    """
    return web.Response(text="Welcome to home page")


async def login_handle(request: web.Request):
    """
    ---
    description: This end-point to login function
    tags:
    - Login
    produces:
    - application/json
    responses:
        "200": CheckResponse
    """
    data = await request.post()
    name = str(data["name"]).lower().replace(" ", "") if "name" in data else None
    ip = data["ip"] if data["ip"] else None
    if name == "ngaongo" and ip:
        session = await get_session(request)
        session["visted"] = True
        session["visted_timestamp"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        session["ip"] = ip
        return web.json_response(
            data={
                "status": 200,
                "result": {"check_status": True},
            }
        )
    return web.json_response(
        data=CheckResponse(
            status=200,
            result=CheckStatus(
                check_status=True, message="Chỉ có ngáo ngơ mới được vào đây"
            ),
        )
    )


async def verify_handle(request: web.Request):
    data = request.query
    ip = data["ip"] if "ip" in data else None
    session = await get_session(request)
    if ip and "ip" in session and session["id"] == ip:
        return web.json_response(
            data=CheckResponse(status=200, result=CheckStatus(check_status=True))
        )

    return web.json_response(
        data=CheckResponse(status=200, result=CheckStatus(check_status=False))
    )
