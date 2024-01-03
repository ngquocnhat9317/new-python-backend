from datetime import datetime, timedelta

from aiohttp import web
from aiohttp_apispec import docs, json_schema, querystring_schema, response_schema
from modules.repositories.logger_repository import LoggerRepository
from modules.repositories.user_repository import UserRepository
from modules.schemas.request_schema import LoginRequest, VerifyRequest
from modules.schemas.response_schema import CheckResponse


@docs(
    tags=["Heath Check"],
    summary="Check heath code",
    description="Check heath code",
    responses={
        200: {
            "description": "Success response",
        },
    },
)
async def welcome(request: web.Request):
    return web.Response(text="Welcome to home page")


@docs(
    tags=["Login Function"],
    summary="Login handle",
    description="Login handle",
    responses={
        200: {
            "schema": CheckResponse,
            "description": "Success response",
        },
    },
)
@json_schema(LoginRequest())
async def login_handle(request: web.Request):
    data = await request.json()
    user_repo = UserRepository(request)

    name = str(data["name"]).lower()
    user = await user_repo.get_user_master()

    ip = str(data["ip"])
    if name in list(user.conditions) and ip:
        logger_repo = LoggerRepository(request)
        logger_repo.login_logger(ip=ip)

        await logger_repo.clear_log()

        return web.json_response(
            CheckResponse().dump(
                {
                    "result": {"check_status": True, "message": "Login Success"},
                }
            )
        )

    return web.json_response(
        CheckResponse().dump(
            {
                "result": {
                    "check_status": False,
                    "message": "Login False",
                }
            }
        )
    )


@docs(
    tags=["Login Function"],
    summary="Verify login status",
    description="Verify login status",
    responses={
        200: {
            "schema": CheckResponse,
            "description": "Success response",
        },
    },
)
@querystring_schema(VerifyRequest())
async def verify_handle(request: web.Request):
    data = request.query
    ip = data["ip"]
    logger_repo = LoggerRepository(request)
    logger_repo.check_logger(ip)

    if logger_repo.check_logger(ip):
        print(CheckResponse().dump({"check_status": True}))
        return web.json_response(CheckResponse().dump({"result": {"check_status": True}}))

    return web.json_response(CheckResponse().dump({"result": {"check_status": False}}))


def check_expired(date_str: str) -> bool:
    time = datetime.strptime(date_str, "%d/%m/%Y, %H:%M:%S")
    return datetime.now() > (time + timedelta(minutes=30))
