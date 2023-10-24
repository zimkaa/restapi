from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from restfull.domain.entities.user import BaseUser
from restfull.infrastructure.database.sqlalchemy import create_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy


router = APIRouter()


@router.get("/{user_id}", summary="Get user", response_model=BaseUser | None)
async def get_user(
    user_id: int,
    db: async_sessionmaker[AsyncSession] = Depends(create_session),
):
    dal = UserRepositorySqlalchemy(db)
    user = await dal.get_by_id(user_id)
    return user
