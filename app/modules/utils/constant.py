import json
import os

from aiohttp import web
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine

load_dotenv()

DATABASE_KEY = web.AppKey("database", AsyncEngine)

LIST_CORRECT_ANSWER = json.loads(os.getenv("LIST_CONDITIONS", "[]"))
