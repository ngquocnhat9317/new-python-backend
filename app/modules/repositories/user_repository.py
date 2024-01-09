from database.db import ConnectPG
from database.models.user_model import User
from database.schemas.user_schema import UserSchema
from modules.repositories import BaseRepository
from modules.utils.constant import LIST_CORRECT_ANSWER
from sqlalchemy import select


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = User
        self.schema = UserSchema()

    async def get_user_by_id(self, id: int) -> User:
        async with self.connect.get_session() as session:
            result = await session.execute(select(User).where(User.id == id))
            return result.scalar_one_or_none()

    async def get_user_master(self) -> User:
        return await self.get_user_by_id(id=1)

    async def init_master(self):
        async with self.connect.get_session() as session:
            result = await session.execute(select(User).where(User.id == 1))
            if result.scalar_one_or_none() is not None:
                session.add(User(id=1, name="Ngao Ngo", conditions=LIST_CORRECT_ANSWER))
                await session.commit()
