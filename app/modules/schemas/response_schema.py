from marshmallow import fields
from modules.schemas import BaseSchema


class BaseResponse(BaseSchema):
    status = fields.Bool(default=True)
    status_code = fields.Integer(strict=True, default=200)


class CheckStatus(BaseSchema):
    check_status = fields.Bool(required=True)
    message = fields.Str()


class ErrorDetail(BaseSchema):
    field = fields.Str()
    error_code = fields.Str(required=True)
    message = fields.Str(required=True)


class CheckResponse(BaseResponse):
    result = fields.Nested(CheckStatus(), required=True)


class CheckStatusResponse(BaseResponse):
    result = fields.Nested(CheckStatus(), required=True)


class ErrorResponse(BaseResponse):
    status = fields.Bool(default=False)
    error_detail = fields.Nested(ErrorDetail(), required=True)
