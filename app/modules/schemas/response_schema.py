from marshmallow import Schema, fields


class BaseResponse(Schema):
    status = fields.Integer(strict=True, default=200)


class CheckStatus(Schema):
    check_status = fields.Bool()
    message = fields.Str()


class CheckResponse(BaseResponse):
    result = fields.Nested(CheckStatus())


class CheckStatusResponse(BaseResponse):
    result = fields.Nested(CheckStatus())
