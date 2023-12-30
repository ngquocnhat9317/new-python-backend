import asyncio
import base64
import logging

import aiohttp_autoreload
from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec
from aiohttp_middlewares import cors_middleware, error_middleware
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from config import DEBUG
from cryptography import fernet
from database.db import engine
from database.models import Base
from modules.repositories.user_repository import UserRepository
from router import routers


def create_database():
    Base.metadata.create_all(engine)


def init_user():
    repo = UserRepository()
    repo.setup_master()


def create_runner():
    app = web.Application(
        middlewares=[
            cors_middleware(allow_all=True),
            error_middleware(),
        ]
    )
    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))
    app.add_routes(routes=routers)

    setup_aiohttp_apispec(app, swagger_path="/docs")
    return web.AppRunner(app)


async def start_server(host="0.0.0.0", port=8080):
    runner = create_runner()
    await runner.setup()

    if DEBUG:
        aiohttp_autoreload.start()
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s: %(message)s", level=logging.DEBUG
    )
    logging.info("Server start")
    site = web.TCPSite(runner, host, port)
    await site.start()


if __name__ == "__main__":
    create_database()
    init_user()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()
