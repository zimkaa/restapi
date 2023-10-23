from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

from restfull.domain.entities.user import BaseUser
from restfull.domain.entities.user import BaseUserWhitPassword
from restfull.infrastructure.database.sqlalchemy import create_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy

router = APIRouter()


@router.put("", summary="Update user", response_model=BaseUser)
async def get_user(
    user: BaseUserWhitPassword,
    db: async_sessionmaker[AsyncSession] = Depends(create_session),
):
    dal = UserRepositorySqlalchemy(db)
    user = await dal.update(user)
    return user
