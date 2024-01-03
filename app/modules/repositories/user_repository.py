from aiohttp import web
from database.models.user_model import User
from database.schemas.user_schema import UserSchema
from modules.repositories import BaseRepository
from modules.utils.constant import LIST_CORRECT_ANSWER


class UserRepository(BaseRepository):
    def __init__(self, request: web.Request):
        super().__init__(request)
        self.model = User
        self.schema = UserSchema()
        self.schema.Meta.sqla_session = self.session

    async def get_user_by_id(self, id: int) -> User:
        return await self.session.query(self.model).filter(self.model.id == id).first()

    async def get_user_master(self) -> User:
        return await self.get_user_by_id(id=1)
