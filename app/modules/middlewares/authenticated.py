from aiohttp import web
from config import ALLOW_TOKEN


@web.middleware
async def authenticated_middleware(request: web.Request, handler):
    if not request.path.startswith("/api/app/"):
        return await handler(request)

    try:
        scheme, token = request.headers["Authorization"].strip().split(" ")
    except KeyError:
        raise web.HTTPUnauthorized(reason="Missing authorization header")
    except ValueError:
        raise web.HTTPForbidden(reason="Invalid authorization header")

    if scheme != "Bearer":
        raise web.HTTPForbidden(reason="Invalid token scheme")
    if token not in ALLOW_TOKEN:
        raise web.HTTPForbidden(reason="Token doesn't exist")

    return await handler(request)