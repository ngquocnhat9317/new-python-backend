from database.models import Base
from database.models.user_model import User
from modules.utils.config import HOST, PASSWORD, PORT, SCHEMA, USER
from modules.utils.logger import logger_info
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from app.modules.utils.constant import LIST_CORRECT_ANSWER


def get_engine() -> AsyncEngine:
    url = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{SCHEMA}"
    return create_async_engine(url)

class ConnectPG:
    def __init__(self):
        self._engine = get_engine()

    @property
    def engine(self):
        return self._engine

    async def init_database(self):
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)
            await conn.execute(insert(User).values(id=1, name='Ngao Ngo', conditions=LIST_CORRECT_ANSWER))

            logger_info("Init database done!")

    def get_session(self) -> AsyncSession:
        return AsyncSession(self._engine)
