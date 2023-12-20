from pydantic import BaseModel


class BaseResponse(BaseModel):
    status: int = 200


class CheckStatus(BaseModel):
    check_status: bool
    message: str = ""



class CheckResponse(BaseResponse):
    result: CheckStatus
