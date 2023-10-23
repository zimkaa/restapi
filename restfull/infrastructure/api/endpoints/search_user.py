from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from restfull.domain.entities.user import BaseUser
from restfull.infrastructure.database.sqlalchemy import create_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy


router = APIRouter()


@router.get("/", summary="Search users", description="Search users by the name", response_model=list[BaseUser])
async def get_user_by_id(
    name: str,
    db: async_sessionmaker[AsyncSession] = Depends(create_session),
):
    if name is None:
        return {"error": "user_id is required"}
    dal = UserRepositorySqlalchemy(db)
    user = await dal.search_user_by_name(name)
    if not user:
        return {"error": "some error"}
    return user
