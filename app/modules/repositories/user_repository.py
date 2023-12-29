from database.models.user_model import User
from database.schemas.user_schema import UserSchema
from modules.repositories import BaseRepository
from modules.utils.constant import LIST_CORRECT_ANSWER


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.model = User
        self.schema = UserSchema()

        self.session_query = self.get_session_query()

    def get_user_by_id(self, id: int) -> User:
        return self.session_query.filter(self.model.id == id).first()

    def setup_master(self):
        user_master = self.get_user_by_id(1)

        if user_master is None:
            self.session.add_all(
                [
                    User(
                        id=1,
                        name="NgaoNgo",
                        conditions=LIST_CORRECT_ANSWER,
                    )
                ]
            )
