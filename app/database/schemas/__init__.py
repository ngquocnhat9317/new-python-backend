from database.db import Session
from marshmallow_sqlalchemy import SQLAlchemySchema


class BaseSchema(SQLAlchemySchema):
    class Meta:
        sqla_session = Session
        load_instance = True
