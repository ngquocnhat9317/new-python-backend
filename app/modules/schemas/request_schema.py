from marshmallow import Schema, fields


class VerifyRequest(Schema):
    ip = fields.Str(description="ip", required=True, allow_none=False)


class LoginRequest(Schema):
    ip = fields.Str(description="ip", required=True, allow_none=False)
    name = fields.Str(description="name", required=True, allow_none=False)
