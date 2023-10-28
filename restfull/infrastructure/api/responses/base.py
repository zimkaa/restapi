from pydantic import BaseModel


class OkResponse(BaseModel):
    result: str = "ok"


class ErrorResponse(BaseModel):
    result: str = "error"
