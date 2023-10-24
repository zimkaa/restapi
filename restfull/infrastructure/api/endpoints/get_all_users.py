from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from restfull.domain.entities.user import BaseUser
from restfull.infrastructure.api.responses.base import OkResponse
from restfull.infrastructure.database.sqlalchemy import create_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy


class BaseListUsersResponse(OkResponse):
    payload: list[BaseUser]


router = APIRouter()


@router.get("", summary="Get all users", response_model=BaseListUsersResponse)
async def get_users(
    db: async_sessionmaker[AsyncSession] = Depends(create_session),
):
    dal = UserRepositorySqlalchemy(db)
    users = await dal.get_all()
    return BaseListUsersResponse(payload=users)
