from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

from restfull.domain.types import UserID
from restfull.infrastructure.database.sqlalchemy import create_session
from restfull.infrastructure.repository.user import UserRepositorySqlalchemy


router = APIRouter()


@router.delete("/{user_id}", summary="Delete user")
async def get_user_by_id(
    user_id: UserID,
    db: async_sessionmaker[AsyncSession] = Depends(create_session),
):
    if user_id is None:
        return {"error": "user_id is required"}
    dal = UserRepositorySqlalchemy(db)
    user = await dal.delete(user_id)
    if not user:
        return {"error": "some error"}
    return {"ok": "user deleted"}
