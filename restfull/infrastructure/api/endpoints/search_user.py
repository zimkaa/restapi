from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from starlette import status

from restfull.domain.entities.user import BaseUser
from restfull.infrastructure.api.responses.base import ErrorResponse
from restfull.infrastructure.api.responses.base import OkResponse
from restfull.infrastructure.database.sqlalchemy import get_async_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy


class ErrorNoUsersResponse(ErrorResponse):
    payload: str = "Users with that name not exist"


class ErrorParameterResponse(ErrorResponse):
    payload: str = "Name query param doesn't exist"


class BaseListUserResponse(OkResponse):
    payload: list[BaseUser]


router = APIRouter()


@router.get(
    "/",
    summary="Search users",
    description="Search users by the name",
    response_model=BaseListUserResponse,
)
async def get_user_by_id(
    name: str,
    db: async_sessionmaker[AsyncSession] = Depends(get_async_session),
):
    if not name:
        return JSONResponse(status_code=status.HTTP_406_NOT_ACCEPTABLE, content=ErrorParameterResponse().model_dump())
    dal = UserRepositorySqlalchemy(db)
    user = await dal.search_user_by_name(name)
    if user:
        return BaseListUserResponse(payload=user)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=ErrorNoUsersResponse().model_dump())
