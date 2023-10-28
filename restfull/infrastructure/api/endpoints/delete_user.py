from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from starlette import status

from restfull.domain.types import UserID
from restfull.infrastructure.api.endpoints.auth import current_user
from restfull.infrastructure.api.responses.base import ErrorResponse
from restfull.infrastructure.api.responses.base import OkResponse
from restfull.infrastructure.database.sqlalchemy import get_async_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy


router = APIRouter()


class ErrorNoUserResponse(ErrorResponse):
    payload: str = "User not exist"


@router.delete(
    "/{user_id}",
    summary="Delete user",
    response_model=OkResponse,
)
async def get_user_by_id(
    user_id: UserID,
    db: async_sessionmaker[AsyncSession] = Depends(get_async_session),
    _=Depends(current_user),
):
    dal = UserRepositorySqlalchemy(db)
    user = await dal.delete(user_id)
    if user:
        return OkResponse()
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=ErrorNoUserResponse().model_dump())
