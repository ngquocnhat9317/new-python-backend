import asyncio

import aiohttp_autoreload
from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec
from aiohttp_middlewares import cors_middleware
from cryptography import fernet
from database.db import ConnectPG
from modules.middlewares.authenticated import authenticated_middleware
from modules.middlewares.error_handle import error_middleware
from modules.utils.config import DEBUG
from modules.utils.logger import logger_info
from router import routers

from app.modules.repositories.user_repository import UserRepository


async def create_runner():
    app = web.Application(
        middlewares=[
            error_middleware,
            cors_middleware(allow_all=True),
            web.normalize_path_middleware(),
            authenticated_middleware,
        ]
    )
    app.add_routes(routes=routers)

    setup_aiohttp_apispec(app, swagger_path="/docs")
    return web.AppRunner(app)


async def start_server(host="0.0.0.0", port=8080):
    runner = await create_runner()
    await runner.setup()

    logger_info("Server start")
    site = web.TCPSite(runner, host, port)
    await site.start()


if __name__ == "__main__":
    connect_pg = ConnectPG()
    user_repo = UserRepository()

    loop = asyncio.get_event_loop()
    asyncio.run_coroutine_threadsafe(connect_pg.init_database(), loop)
    if DEBUG:
        aiohttp_autoreload.start(loop)
    loop.run_until_complete(start_server())
    loop.run_forever()
