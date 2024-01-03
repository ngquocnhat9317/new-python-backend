from aiohttp import web
from sqlalchemy.ext.asyncio import AsyncEngine

DATABASE_KEY = web.AppKey("database", AsyncEngine)

LIST_CORRECT_ANSWER = [
    "ngáo",
    "ngáo ngơ",
    "đồ ngốc nghếch",
    "đồ vợ hư",
    "cục cưng",
    "cục cức",
    "thuỳ trang",
    "thuỳ ngáo",
    "lê thị thuỳ ngáo",
    "thị ngáo",
]
