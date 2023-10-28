from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from restfull.domain.entities.user import BaseUser
from restfull.infrastructure.api.responses.base import ErrorResponse
from restfull.infrastructure.api.responses.base import OkResponse
from restfull.infrastructure.database.sqlalchemy import get_async_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy


router = APIRouter()


class BaseUserResponse(OkResponse):
    payload: BaseUser


class ErrorUserResponse(ErrorResponse):
    payload: str = "User not found"


@router.get(
    "/{user_id}",
    summary="Get user by id",
    response_model=BaseUserResponse,
)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_async_session),
):
    dal = UserRepositorySqlalchemy(db)
    user = await dal.get_by_id(user_id)
    if user:
        return BaseUserResponse(payload=user)
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=ErrorUserResponse().model_dump())
