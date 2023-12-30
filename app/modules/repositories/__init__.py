from database.schemas import Session


class ModelError(Exception):
    pass


class SchemaError(Exception):
    pass


class BaseRepository:
    def __init__(self):
        super().__init__()
        self.session = Session
        self.schema = None
        self.model = None

    def get_session_query(self):
        if self.model is None:
            raise ModelError()
        return self.session.query(self.model)

    def serialization(self, unserialization):
        if self.schema is None:
            raise SchemaError()
        return self.schema.dump(unserialization)
