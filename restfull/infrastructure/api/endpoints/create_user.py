from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from starlette import status

from restfull.infrastructure.api.responses.base import ErrorResponse
from restfull.infrastructure.api.responses.base import OkResponse
from restfull.domain.entities.user import UserWhitPassword
from restfull.infrastructure.database.sqlalchemy import create_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy


class UnknownErrorResponse(ErrorResponse):
    payload: str = "See logs"


class ErrorBodyParameterResponse(ErrorResponse):
    payload: str = "Body parameters is empty"

router = APIRouter()


@router.post("", summary="Create user", response_model=OkResponse)
async def create(
    user: UserWhitPassword,
    db: async_sessionmaker[AsyncSession] = Depends(create_session),
):
    if user == UserWhitPassword():
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content=ErrorBodyParameterResponse().model_dump())
    dal = UserRepositorySqlalchemy(db)
    user = await dal.create(user)
    if user:
        return OkResponse()
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=UnknownErrorResponse().model_dump())
