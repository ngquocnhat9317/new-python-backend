from database.models.logger_model import Logger
from database.schemas import BaseSchema
from marshmallow_sqlalchemy import auto_field


class LoggerSchema(BaseSchema):
    class Meta(BaseSchema.Meta):
        model = Logger  # Optional: deserialize to model instances

    id: auto_field()
    logger_ip: auto_field()
    create_at: auto_field()
