from config import DATABASE, HOST, PASSWD, PORT, USER
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


def get_engine() -> AsyncEngine:
    url = f"postgresql+asyncpg://{USER}:{PASSWD}@{HOST}:{PORT}/{DATABASE}"
    return create_async_engine(url)
