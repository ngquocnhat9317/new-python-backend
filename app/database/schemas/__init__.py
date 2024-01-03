from marshmallow_sqlalchemy import SQLAlchemySchema


class BaseSQLSchema(SQLAlchemySchema):
    class Meta:
        load_instance = True
