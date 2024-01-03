from aiohttp import web
from modules.controllers.home_controller import (login_handle, verify_handle,
                                                 welcome)

routers = [
    web.get("/", welcome, allow_head=False),
    web.post("/api/app/login", login_handle),
    web.get("/api/app/verify", verify_handle, allow_head=False),
]
