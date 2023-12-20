import asyncio
import base64

from aiohttp import web
from aiohttp_middlewares import cors_middleware, error_middleware
from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from cryptography import fernet
from router import routers
from aiohttp_swagger import setup_swagger


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

    setup_swagger(app, swagger_url="/docs", title="Demo Swagger API")

    return web.AppRunner(app)


async def start_server(host="0.0.0.0", port=8080):
    runner = create_runner()
    await runner.setup()

    site = web.TCPSite(runner, host, port)
    await site.start()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_server())
    loop.run_forever()
