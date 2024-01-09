from aiohttp import web
from modules.utils.constant import DATABASE_KEY
from sqlalchemy.ext.asyncio import AsyncSession


class ModelError(Exception):
    pass


class SchemaError(Exception):
    pass


class SessionError(Exception):
    pass


class BaseRepository:
    def __init__(self):
        self.schema = None
        self.model = None

    def serialization(self, unserialization):
        if self.schema is None:
            raise SchemaError()
        return self.schema.dump(unserialization)

    async def close(self):
        await self.session.close()
