from aiohttp import web
from database.db import ConnectPG


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
        self.connect = ConnectPG()

    def serialization(self, unserialization):
        if self.schema is None:
            raise SchemaError()
        return self.schema.dump(unserialization)

    async def close(self):
        await self.session.close()
