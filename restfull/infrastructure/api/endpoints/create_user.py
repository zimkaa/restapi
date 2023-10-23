from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

# from restfull.domain.entities.user import BaseUser
from restfull.domain.entities.user import UserWhitPassword
from restfull.infrastructure.database.sqlalchemy import create_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy

router = APIRouter()


@router.post("", summary="Create user")
async def create(
    user: UserWhitPassword,
    db: async_sessionmaker[AsyncSession] = Depends(create_session),
):
    dal = UserRepositorySqlalchemy(db)
    user = await dal.create(user)
    return user
