from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from restfull.domain.entities.user import BaseUser
from restfull.domain.entities.user import BaseUserWhitPassword
from restfull.infrastructure.api.responses.base import ErrorResponse
from restfull.infrastructure.api.responses.base import OkResponse
from restfull.infrastructure.database.sqlalchemy import create_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy


class ErrorWithUpdateResponse(ErrorResponse):
    payload: str = "See logs"


class BaseUpdateUserResponse(OkResponse):
    payload: BaseUser


router = APIRouter()


@router.put("", summary="Update user", response_model=BaseUpdateUserResponse)
async def get_user(
    user: BaseUserWhitPassword,
    db: async_sessionmaker[AsyncSession] = Depends(create_session),
):
    dal = UserRepositorySqlalchemy(db)
    updated_user = await dal.update(user)
    if updated_user:
        return BaseUpdateUserResponse(payload=updated_user)
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=ErrorWithUpdateResponse().model_dump())
