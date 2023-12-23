from datetime import datetime, timedelta

from aiohttp import web
from aiohttp_apispec import docs, json_schema, querystring_schema, response_schema
from aiohttp_session import get_session
from modules.utils.constant import LIST_CORRECT_ANSWER
from modules.schemas.request_schema import LoginRequest, VerifyRequest
from modules.schemas.response_schema import CheckResponse, CheckStatus


@docs(
    tags=["Heath Check"],
    summary="Check heath code",
    description="Check heath code",
)
async def welcome(request: web.Request):
    return web.Response(text="Welcome to home page")


@docs(
    tags=["Login Function"],
    summary="Login handle",
    description="Login handle",
)
@json_schema(LoginRequest())
@response_schema(CheckResponse(), 200)
async def login_handle(request: web.Request):
    data = await request.json()
    name = str(data["name"]).lower()
    ip = data["ip"]
    if name in LIST_CORRECT_ANSWER and ip:
        session = await get_session(request)
        session["visted"] = True
        session["visted_timestamp"] = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        session["ip"] = ip
        return web.json_response(
            data={
                "status": 200,
                "result": {"check_status": True, "message": "Login Success"},
            }
        )
    return web.json_response(
        data={
            "status": 200,
            "result": {
                "check_status": False,
                "message": "Login False",
            },
        }
    )


@docs(
    tags=["Login Function"],
    summary="Verify login status",
    description="Verify login status",
)
@querystring_schema(VerifyRequest())
@response_schema(CheckResponse(), 200)
async def verify_handle(request: web.Request):
    data = request.query
    ip = data["ip"] if "ip" in data else None
    session = await get_session(request)

    if (
        "ip" not in session
        or session["ip"] != ip
        or "visted_timestamp" not in session
        or check_expired(session["visted_timestamp"])
    ):
        return web.json_response(
            data={
                "status": 200,
                "result": {"check_status": False},
            }
        )

    return web.json_response(
        data={
            "status": 200,
            "result": {"check_status": True},
        }
    )


def check_expired(date_str: str) -> bool:
    time = datetime.strptime(date_str, "%d/%m/%Y, %H:%M:%S")
    return datetime.now() > (time + timedelta(minutes=30))
